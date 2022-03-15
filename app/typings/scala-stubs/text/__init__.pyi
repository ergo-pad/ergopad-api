import java.io
import scala
import scala.collection
import typing



class DocBreak:
    @typing.overload
    @staticmethod
    def $colon$colon(hd: str) -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$colon(hd: 'Document') -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$div$colon(hd: str) -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$div$colon(hd: 'Document') -> 'Document': ...
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def format(width: int, writer: java.io.Writer) -> None: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def productArity() -> int: ...
    @staticmethod
    def productElement(x$1: int) -> typing.Any: ...
    @staticmethod
    def productIterator() -> scala.collection.Iterator[typing.Any]: ...
    @staticmethod
    def productPrefix() -> str: ...
    @staticmethod
    def toString() -> str: ...

class DocNil:
    @typing.overload
    @staticmethod
    def $colon$colon(hd: str) -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$colon(hd: 'Document') -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$div$colon(hd: str) -> 'Document': ...
    @typing.overload
    @staticmethod
    def $colon$div$colon(hd: 'Document') -> 'Document': ...
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def format(width: int, writer: java.io.Writer) -> None: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def productArity() -> int: ...
    @staticmethod
    def productElement(x$1: int) -> typing.Any: ...
    @staticmethod
    def productIterator() -> scala.collection.Iterator[typing.Any]: ...
    @staticmethod
    def productPrefix() -> str: ...
    @staticmethod
    def toString() -> str: ...

class Document:
    def __init__(self): ...
    @typing.overload
    def $colon$colon(self, hd: str) -> 'Document': ...
    @typing.overload
    def $colon$colon(self, hd: 'Document') -> 'Document': ...
    @typing.overload
    def $colon$div$colon(self, hd: str) -> 'Document': ...
    @typing.overload
    def $colon$div$colon(self, hd: 'Document') -> 'Document': ...
    @staticmethod
    def empty() -> 'DocNil.': ...
    def format(self, width: int, writer: java.io.Writer) -> None: ...
    @staticmethod
    def group(d: 'Document') -> 'Document': ...
    @staticmethod
    def nest(i: int, d: 'Document') -> 'Document': ...
    @staticmethod
    def text(s: str) -> 'Document': ...

class DocCons(Document, scala.Product, scala.Serializable):
    def __init__(self, hd: Document, tl: Document): ...
    @staticmethod
    def apply(hd: Document, tl: Document) -> 'DocCons': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def copy(self, hd: Document, tl: Document) -> 'DocCons': ...
    def copy$default$1(self) -> Document: ...
    def copy$default$2(self) -> Document: ...
    @staticmethod
    def curried() -> scala.Function1[Document, scala.Function1[Document, 'DocCons']]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def hd(self) -> Document: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def tl(self) -> Document: ...
    def toString(self) -> str: ...
    @staticmethod
    def tupled() -> scala.Function1[scala.Tuple2[Document, Document], 'DocCons']: ...
    @staticmethod
    def unapply(x$0: 'DocCons') -> scala.Option[scala.Tuple2[Document, Document]]: ...

class DocGroup(Document, scala.Product, scala.Serializable):
    def __init__(self, doc: Document): ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    @staticmethod
    def andThen(g: scala.Function1['DocGroup', _andThen__A]) -> scala.Function1[Document, _andThen__A]: ...
    @staticmethod
    def apply(doc: Document) -> 'DocGroup': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    @staticmethod
    def compose(g: scala.Function1[_compose__A, Document]) -> scala.Function1[_compose__A, 'DocGroup']: ...
    def copy(self, doc: Document) -> 'DocGroup': ...
    def copy$default$1(self) -> Document: ...
    def doc(self) -> Document: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'DocGroup') -> scala.Option[Document]: ...

class DocNest(Document, scala.Product, scala.Serializable):
    def __init__(self, indent: int, doc: Document): ...
    @staticmethod
    def apply(indent: int, doc: Document) -> 'DocNest': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def copy(self, indent: int, doc: Document) -> 'DocNest': ...
    def copy$default$1(self) -> int: ...
    def copy$default$2(self) -> Document: ...
    @staticmethod
    def curried() -> scala.Function1[typing.Any, scala.Function1[Document, 'DocNest']]: ...
    def doc(self) -> Document: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def indent(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def tupled() -> scala.Function1[scala.Tuple2[typing.Any, Document], 'DocNest']: ...
    @staticmethod
    def unapply(x$0: 'DocNest') -> scala.Option[scala.Tuple2[typing.Any, Document]]: ...

class DocText(Document, scala.Product, scala.Serializable):
    def __init__(self, txt: str): ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    @staticmethod
    def andThen(g: scala.Function1['DocText', _andThen__A]) -> scala.Function1[str, _andThen__A]: ...
    @staticmethod
    def apply(txt: str) -> 'DocText': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    @staticmethod
    def compose(g: scala.Function1[_compose__A, str]) -> scala.Function1[_compose__A, 'DocText']: ...
    def copy(self, txt: str) -> 'DocText': ...
    def copy$default$1(self) -> str: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    def txt(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'DocText') -> scala.Option[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.text")``.

    DocBreak: typing.Type[DocBreak]
    DocCons: typing.Type[DocCons]
    DocGroup: typing.Type[DocGroup]
    DocNest: typing.Type[DocNest]
    DocNil: typing.Type[DocNil]
    DocText: typing.Type[DocText]
    Document: typing.Type[Document]
