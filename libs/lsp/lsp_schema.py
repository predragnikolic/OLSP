from typing import List, Literal, TypedDict, Union
from typing_extensions import NotRequired

_Type = Union["BaseType", "ReferenceType", "ArrayType", "MapType", "AndType", "OrType", "TupleType", "StructureLiteralType", "StringLiteralType", "IntegerLiteralType", "BooleanLiteralType"]
_BaseTypes = Literal["Uri", "DocumentUri", "integer", "uinteger", "decimal", "RegExp", "string", "boolean", "null"]

class EnumerationType(TypedDict):
    kind: Literal['base']
    name: Literal["string", "integer", "uinteger"]

class EnumerationEntry(TypedDict):
    documentation: NotRequired[str]
    name: str
    proposed: NotRequired[bool]
    since: NotRequired[str]
    value: Union[str, int]

class ReferenceType(TypedDict):
    """Represents a reference to another type (e.g. `TextDocument`). This is either a `Structure`, a `Enumeration` or a `TypeAlias` in the same meta model."""
    kind: Literal['reference']
    name: Literal["string", "integer", "uinteger"]

class Property(TypedDict):
    documentation: NotRequired[str]
    name: str
    optional: NotRequired[bool]
    proposed: NotRequired[bool]
    since: NotRequired[str]
    type: _Type

class StringLiteralType(TypedDict):
    """Represents a string literal type (e.g. `kind: 'rename'`)."""
    kind: Literal['stringLiteral']
    value: str

class AndType(TypedDict):
    """ Represents an `and`type (e.g. TextDocumentParams & WorkDoneProgressParams`). """
    items: List[_Type]
    kind: Literal["and"]

class OrType(TypedDict):
    """Represents an `or` type (e.g. `Location | LocationLink`). """
    items: List[_Type]
    kind: Literal["or"]

class ArrayType(TypedDict):
    """ Represents an array type (e.g. `TextDocument[]`). """
    element: List[_Type]
    kind: Literal["array"]

class BaseType(TypedDict):
    """Represents a base type like `string` or `DocumentUri`. """
    name: _BaseTypes
    kind: Literal["base"]

class BooleanLiteralType(TypedDict):
    """Represents a boolean literal type (e.g. `kind: true`). """
    value: bool
    kind: Literal["booleanLiteral"]

class Enumeration(TypedDict):
    documentation: NotRequired[str]
    name: str
    proposed: NotRequired[bool]
    since: NotRequired[str]
    supportsCustomValues: NotRequired[bool]
    type: EnumerationType
    values: List[EnumerationEntry]

class IntegerLiteralType(TypedDict):
    value: int
    kind: Literal["integerLiteral"]
    """Represents an integer literal type (e.g. `kind: 1`)."""

class _MapKeyType_1(TypedDict):
    kind: Literal["base"]
    name: Literal["Uri", "DocumentUri", "string", "integer"]

MapKeyType = Union[_MapKeyType_1, ReferenceType]
"""Represents a type that can be used as a key in a map type. If a reference type is used then the type must either resolve to a `string` or `integer` type. (e.g. `type ChangeAnnotationIdentifier === string`)."""

class MapType(TypedDict):
    key: MapKeyType
    kind: Literal["map"]
    value: _Type

MessageDirection = Literal["clientToServer", "serverToClient", "both"]
"""Indicates in which direction a message is sent in the protocol."""

class Notification(TypedDict):
    documentation: NotRequired[str]
    messageDirection: MessageDirection
    method: str
    params: NotRequired[Union[_Type, List[_Type]]]
    proposed: NotRequired[bool]
    registrationMethod: NotRequired[str]
    """Optional a dynamic registration method if it different from the request's method."""
    registrationOptions: NotRequired[_Type]
    """Optional registration options if the notification supports dynamic registration."""
    since: NotRequired[str]


class Request(TypedDict):
    documentation: NotRequired[str]
    errorData: NotRequired[_Type]
    messageDirection: MessageDirection
    method: str
    params: NotRequired[Union[_Type, List[_Type]]]
    partialResult: NotRequired[_Type]
    proposed: NotRequired[bool]
    registrationMethod: NotRequired[str]
    registrationOptions: NotRequired[_Type]
    result: _Type
    since: NotRequired[str]

class Structure(TypedDict):
    documentation: NotRequired[str]
    extends: NotRequired[List[_Type]]
    """Structures extended from. This structures form a polymorphic type hierarchy."""
    mixins: NotRequired[List[_Type]]
    """Structures to mix in. The properties of these structures are `copied` into this structure. Mixins don't form a polymorphic type hierarchy in LSP."""
    name: str
    properties: List[Property]
    proposed: NotRequired[bool]
    since: NotRequired[str]

class StructureLiteral(TypedDict):
    """Defines a unnamed structure of an object literal."""
    documentation: NotRequired[str]
    properties: List[Property]
    proposed: NotRequired[bool]
    since: NotRequired[str]


class StructureLiteralType(TypedDict):
    """Represents a literal structure (e.g. `property: { start: uinteger; end: uinteger; }`)."""
    kind: Literal["literal"]
    value: StructureLiteral

class TupleType(TypedDict):
    """Represents a `tuple` type (e.g. `[integer, integer]`)."""
    kind: Literal["tuple"]
    items: List[_Type]

class TypeAlias(TypedDict):
    """ Defines a type alias. (e.g. `type Definition = Location | LocationLink`)"""
    documentation: NotRequired[str]
    name: str
    proposed: NotRequired[bool]
    since: NotRequired[str]
    type: _Type

class MetaModel(TypedDict):
    enumerations: List[Enumeration]
    notifications: List[Notification]
    requests: List[Request]
    structures: List[Structure]
    typeAliases: List[TypeAlias]

TypeKind = Literal["base", "reference", "array", "map", "and", "or", "tuple", "literal", "stringLiteral", "integerLiteral", "booleanLiteral"]