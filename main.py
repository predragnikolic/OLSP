import asyncio
import os
from re import sub
from typing import List

from event_loop import wait
from lsp.server import LanguageServer
from lsp.types import CompletionParams
import sublime

import sublime_plugin
from sublime_types import Point

servers: List[LanguageServer] = []

async def main():
    global servers
    server = LanguageServer('typescript-language-server --stdio')
    await server.start()

    def on_log_message(x):
        print('handle log message', x)

    server.on_notification('window/logMessage', on_log_message)
    await server.send.initialize(({
        'processId': os.getpid(),
        'rootUri': None,
        'capabilities': {}
    }))
    servers.append(server)

@wait
async def plugin_loaded() -> None:
    await main()

class DocumentListener(sublime_plugin.ViewEventListener):
    def on_load(self):
        file_name = self.view.file_name()
        if not file_name:
            return
        print('opened', file_name)
        for server in servers:
            server.notify.did_open_text_document({
                'textDocument': {
                    'version': self.view.change_count(),
                    'languageId': 'javascript',
                    'text': self.view.substr(self.view.size()),
                    'uri': 'file://' + file_name
                }
            })

    def on_close(self):
        file_name = self.view.file_name()
        if not file_name:
            return
        for server in servers:
            server.notify.did_close_text_document({
                'textDocument': {
                    'uri': 'file://' + file_name
                }
            })

    def on_query_completions(self, prefix: str, locations: List[Point]):
        completion_list = sublime.CompletionList()
        file_name = self.view.file_name()
        if not file_name:
            return
        row, col = self.view.rowcol(locations[0])
        params: CompletionParams = {
            'position': {'line': row, 'character': col},
            'textDocument': {
                'uri': 'file://' + file_name
            }
        }
        asyncio.ensure_future(self.do_completions(completion_list, params))
        return completion_list

    @wait
    async def do_completions(self, completion_list: sublime.CompletionList, params: CompletionParams):
        completions: List[sublime.CompletionItem] = []
        for server in servers:
            res = await server.send.completion(params)
            if isinstance(res, dict):
                items = res['items']
                for i in items:
                    completions.append(sublime.CompletionItem(i['label']))
        completion_list.set_completions(completions)
