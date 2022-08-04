from enum import Enum
from typing import Any, Dict, Literal, Optional, Union, List
from typing_extensions import TypedDict, NotRequired


ProgressToken = Union[int, str]

DocumentUri = str

TraceValue = Union[Literal['off'],  Literal['messages'],  Literal['verbose']]

TextDocumentClientCapabilities = Dict

NotebookDocumentClientCapabilities = Dict

DiagnosticWorkspaceClientCapabilities = Dict

WorkspaceEditClientCapabilities = Dict

DidChangeConfigurationClientCapabilities = Dict

DidChangeWatchedFilesClientCapabilities = Dict

class SymbolKind(Enum):
    File = 1
    Module = 2
    Namespace = 3
    Package = 4
    Class = 5
    Method = 6
    Property = 7
    Field = 8
    Constructor = 9
    Enum = 10
    Interface = 11
    Function = 12
    Variable = 13
    Constant = 14
    String = 15
    Number = 16
    Boolean = 17
    Array = 18
    Object = 19
    Key = 20
    Null = 21
    EnumMember = 22
    Struct = 23
    Event = 24
    Operator = 25
    TypeParameter = 26


class SymbolTag(Enum):
    Deprecated = 1;

class WorkspaceSymbolClientCapabilities_SymbolKind(TypedDict):
    valueSet: NotRequired[List[SymbolKind]]
    """
    The symbol kind values the client supports. When this
    property exists the client also guarantees that it will
    handle values outside its set gracefully and falls back
    to a default value when unknown.

    If this property is not present the client only supports
    the symbol kinds from `File` to `Array` as defined in
    the initial version of the protocol.
    """

class WorkspaceSymbolClientCapabilities_TagSupport(TypedDict):
    valueSet: List[SymbolTag]
    """
    The tags supported by the client.
    """

class WorkspaceSymbolClientCapabilities(TypedDict):
    dynamicRegistration: NotRequired[bool]
    """
    Symbol request supports dynamic registration.
    """

    symbolKind: NotRequired[WorkspaceSymbolClientCapabilities_SymbolKind]
    """
    Specific capabilities for the `SymbolKind` in the
    `textDocument/documentSymbol` request.
    """


    hierarchicalDocumentSymbolSupport: NotRequired[bool]
    """
    The client supports hierarchical document symbols.
    """

    tagSupport: NotRequired[WorkspaceSymbolClientCapabilities_TagSupport]
    """
    The client supports tags on `SymbolInformation`. Tags are supported on
    `DocumentSymbol` if `hierarchicalDocumentSymbolSupport` is set to true.
    Clients supporting tags have to handle unknown tags gracefully.

    @since 3.16.0
    """

    labelSupport: NotRequired[bool]
    """
    The client supports an additional label presented in the UI when
    registering a document symbol provider.

    @since 3.16.0
    """

class ExecuteCommandClientCapabilities(TypedDict):
    dynamicRegistration: NotRequired[bool]
    """
    Execute command supports dynamic registration.
    """

class SemanticTokensWorkspaceClientCapabilities(TypedDict):
    refreshSupport: NotRequired[bool]
    """
    Whether the client implementation supports a refresh request sent from
    the server to the client.

    Note that this event is global and will force the client to refresh all
    semantic tokens currently shown. It should be used with absolute care
    and is useful for situation where a server for example detect a project
    wide change that requires such a calculation.
    """

class CodeLensWorkspaceClientCapabilities(TypedDict):
    refreshSupport: NotRequired[bool]
    """
    Whether the client implementation supports a refresh request sent from
    the server to the client.

    Note that this event is global and will force the client to refresh all
    code lenses currently shown. It should be used with absolute care and is
    useful for situation where a server for example detect a project wide
    change that requires such a calculation.
    """


class InlineValueWorkspaceClientCapabilities(TypedDict):
    refreshSupport: NotRequired[bool]
    """
    Whether the client implementation supports a refresh request sent from
    the server to the client.

    Note that this event is global and will force the client to refresh all
    inline values currently shown. It should be used with absolute care and
    is useful for situation where a server for example detect a project wide
    change that requires such a calculation.
    """

class InlayHintWorkspaceClientCapabilities(TypedDict):
    refreshSupport: NotRequired[bool]
    """
    Whether the client implementation supports a refresh request sent from
    the server to the client.

    Note that this event is global and will force the client to refresh all
    inlay hints currently shown. It should be used with absolute care and
    is useful for situation where a server for example detects a project wide
    change that requires such a calculation.
    """

class ShowMessageRequestClientCapabilities_MessageActionItem(TypedDict):
    additionalPropertiesSupport: NotRequired[bool]
    """
    Whether the client supports additional attributes which
    are preserved and sent back to the server in the
    request's response.
    """

class ShowMessageRequestClientCapabilities(TypedDict):
    messageActionItem: NotRequired[ShowMessageRequestClientCapabilities_MessageActionItem]
    """
    Capabilities specific to the `MessageActionItem` type.
    """

class ShowDocumentClientCapabilities(TypedDict):
    support: bool
    """
    The client has support for the show document
    request.
    """

class RegularExpressionsClientCapabilities(TypedDict):
    engine: str
    """
    The engine's name.
    """

    version: NotRequired[str]
    """
    The engine's version.
    """

class MarkdownClientCapabilities(TypedDict):
    parser: str
    """
    The name of the parser.
    """

    version: NotRequired[str]
    """
    The version of the parser.
    """

    allowedTags: NotRequired[List[str]]
    """
    A list of HTML tags that the client allows / supports in Markdown.

    @since 3.17.0
    """

PositionEncodingKind = str

class WorkDoneProgressParams(TypedDict):
    workDoneToken: NotRequired[ProgressToken]
    """
    An optional token that a server can use to report work done progress.
    """

class ClientInfo(TypedDict):
    name: str
    """ The name of the client as defined by the client. """

    version: NotRequired[str]
    """ The client's version as defined by the client. """

class WorkspaceFolder(TypedDict):
    uri: DocumentUri
    """ The associated URI for this workspace folder. """

    name: NotRequired[str]
    """
    The name of the workspace folder. Used to refer to this
    workspace folder in the user interface.
    """

class ClientCapabilities_Workspace_FileOperations(TypedDict):
    dynamicRegistration: NotRequired[bool]
    """
    Whether the client supports dynamic registration for file
    requests/notifications.
    """

    didCreate: NotRequired[bool]
    """
    The client has support for sending didCreateFiles notifications.
    """

    willCreate: NotRequired[bool]
    """
    The client has support for sending willCreateFiles requests.
    """

    didRename: NotRequired[bool]
    """
    The client has support for sending didRenameFiles notifications.
    """

    willRename: NotRequired[bool]
    """
    The client has support for sending willRenameFiles requests.
    """

    didDelete: NotRequired[bool]
    """
    The client has support for sending didDeleteFiles notifications.
    """

    willDelete: NotRequired[bool]
    """
    The client has support for sending willDeleteFiles requests.
    """

class ClientCapabilities_Workspace(TypedDict):
    applyEdit: NotRequired[bool]
    """
    The client supports applying batch edits
    to the workspace by supporting the request
    'workspace/applyEdit'
    """

    workspaceEdit: NotRequired[WorkspaceEditClientCapabilities]
    """
    Capabilities specific to `WorkspaceEdit`s
    """

    didChangeConfiguration: NotRequired[DidChangeConfigurationClientCapabilities]
    """
    Capabilities specific to the `workspace/didChangeConfiguration`
    notification.
    """

    didChangeWatchedFiles: NotRequired[DidChangeWatchedFilesClientCapabilities]
    """
    Capabilities specific to the `workspace/didChangeWatchedFiles`
    notification.
    """


    symbol: NotRequired[WorkspaceSymbolClientCapabilities]
    """
    Capabilities specific to the `workspace/symbol` request.
    """

    executeCommand: NotRequired[ExecuteCommandClientCapabilities]
    """
    Capabilities specific to the `workspace/executeCommand` request.
    """

    workspaceFolders: NotRequired[bool]
    """
    The client has support for workspace folders.

    @since 3.6.0
    """

    configuration: NotRequired[bool]
    """
    The client supports `workspace/configuration` requests.

    @since 3.6.0
    """

    semanticTokens: NotRequired[SemanticTokensWorkspaceClientCapabilities]
    """
    Capabilities specific to the semantic token requests scoped to the
    workspace.

    @since 3.16.0
    """

    codeLens: NotRequired[CodeLensWorkspaceClientCapabilities]
    """
    Capabilities specific to the code lens requests scoped to the
    workspace.

    @since 3.16.0
    """

    fileOperations: NotRequired[ClientCapabilities_Workspace_FileOperations]
    """
    The client has support for file requests/notifications.

    @since 3.16.0
    """

    inlineValue: NotRequired[InlineValueWorkspaceClientCapabilities]
    """
    Client workspace capabilities specific to inline values.

    @since 3.17.0
    """

    inlayHint: NotRequired[InlayHintWorkspaceClientCapabilities]
    """
    Client workspace capabilities specific to inlay hints.

    @since 3.17.0
    """

    diagnostics: NotRequired[DiagnosticWorkspaceClientCapabilities]
    """
    Client workspace capabilities specific to diagnostics.

    @since 3.17.0.
    """

class ClientCapabilities_Window(TypedDict):
    workDoneProgress: NotRequired[bool]
    """
    It indicates whether the client supports server initiated
    progress using the `window/workDoneProgress/create` request.

    The capability also controls Whether client supports handling
    of progress notifications. If set servers are allowed to report a
    `workDoneProgress` property in the request specific server
    capabilities.

    @since 3.15.0
    """

    showMessage: NotRequired[ShowMessageRequestClientCapabilities]
    """
    Capabilities specific to the showMessage request

    @since 3.16.0
    """

    showDocument: NotRequired[ShowDocumentClientCapabilities]
    """
    Client capabilities for the show document request.

    @since 3.16.0
    """

class ClientCapabilities_General_StaleRequestSupport(TypedDict):
    cancel: bool
    """
    The client will actively cancel the request.
    """

    retryOnContentModified: List[str]
    """
    The list of requests for which the client
    will retry the request if it receives a
    response with error code `ContentModified``
    """

class ClientCapabilities_General(TypedDict):
    staleRequestSupport: NotRequired[ClientCapabilities_General_StaleRequestSupport]
    """
    Client capability that signals how the client
    handles stale requests (e.g. a request
    for which the client will not process the response
    anymore since the information is outdated).

    @since 3.17.0
    """

    regularExpressions: NotRequired[RegularExpressionsClientCapabilities]
    """
    Client capabilities specific to regular expressions.

    @since 3.16.0
    """

    markdown: NotRequired[MarkdownClientCapabilities]
    """
    Client capabilities specific to the client's markdown parser.

    @since 3.16.0
    """

    positionEncodings: NotRequired[List[PositionEncodingKind]]
    """
    The position encodings supported by the client. Client and server
    have to agree on the same position encoding to ensure that offsets
    (e.g. character position in a line) are interpreted the same on both
    side.

    To keep the protocol backwards compatible the following applies: if
    the value 'utf-16' is missing from the array of position encodings
    servers can assume that the client supports UTF-16. UTF-16 is
    therefore a mandatory encoding.

    If omitted it defaults to ['utf-16'].

    Implementation considerations: since the conversion from one encoding
    into another requires the content of the file / line the conversion
    is best done where the file is read which is usually on the server
    side.

    @since 3.17.0
    """

class ClientCapabilities(TypedDict):
    workspace: NotRequired[ClientCapabilities_Workspace]
    """
    Workspace specific client capabilities.
    """

    textDocument: NotRequired[TextDocumentClientCapabilities]
    """
    Text document specific client capabilities.
    """

    notebookDocument: NotRequired[NotebookDocumentClientCapabilities]
    """
    Capabilities specific to the notebook document support.

    @since 3.17.0
    """

    window: NotRequired[ClientCapabilities_Window]
    """
    Window specific client capabilities.
    """

    general: NotRequired[ClientCapabilities_General]
    """
    General client capabilities.

    @since 3.16.0
    """

    experimental: NotRequired[Any]
    """
    Experimental client capabilities.
    """

class  InitializeParams(WorkDoneProgressParams):
    processId: Optional[int]
    """
    The process Id of the parent process that started the server. Is null if
    the process has not been started by another process. If the parent
    process is not alive then the server should exit (see exit notification)
    its process.
    """

    clientInfo: NotRequired[ClientInfo]
    """
    Information about the client
    @since 3.15.0
    """

    locale: NotRequired[str]
    """
    The locale the client is currently showing the user interface
    in. This must not necessarily be the locale of the operating
    system.

    Uses IETF language tags as the value's syntax
    (See https://en.wikipedia.org/wiki/IETF_language_tag)
    @since 3.16.0
    """

    initializationOptions: NotRequired[Any]
    """
    User provided initialization options.
    """

    capabilities: ClientCapabilities
    """
    The capabilities provided by the client (editor or tool)
    """

    trace: NotRequired[TraceValue]
    """
    The initial trace setting. If omitted trace is disabled ('off').
    """

    workspaceFolders: NotRequired[Optional[List[WorkspaceFolder]]]
    """
    The workspace folders configured in the client when the server starts.
    This property is only available if the client supports workspace folders.
    It can be `null` if the client supports workspace folders but none are
    configured.

    @since 3.6.0
    """

