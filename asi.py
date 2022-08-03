import asyncio
from .lsp_specification import ClientCapabilities, SymbolTag
import sublime_plugin
from .event_loop import wait

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

@wait
async def plugin_loaded() -> None:
    await main()

class TextCommand(sublime_plugin.TextCommand):
    @wait
    async def run(self, edit):
        try:
            await asyncio.gather(request(), request(), request(), request(), request())
        except:
            print('here')

c: ClientCapabilities = {
    'workspace': {
        'symbol': {
            'tagSupport': {
                'valueSet': [SymbolTag.Deprecated]
            }
        }
    }
}

count = 1
async def request():
    global count
    id = count
    count += 1
    print('fire', id)
    await asyncio.sleep(1)
    print('done', id)