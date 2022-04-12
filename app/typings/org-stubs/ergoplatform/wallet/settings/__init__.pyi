import cats.data
import io.circe
import scala
import scala.collection
import scala.collection.immutable
import scala.util
import typing



class EncryptionSettings(scala.Product, scala.Serializable):
    def __init__(self, prf: str, c: int, dkLen: int): ...
    @staticmethod
    def apply(prf: str, c: int, dkLen: int) -> 'EncryptionSettings': ...
    def c(self) -> int: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def copy(self, prf: str, c: int, dkLen: int) -> 'EncryptionSettings': ...
    def copy$default$1(self) -> str: ...
    def copy$default$2(self) -> int: ...
    def copy$default$3(self) -> int: ...
    def dkLen(self) -> int: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def prf(self) -> str: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'EncryptionSettings') -> scala.Option[scala.Tuple3[str, typing.Any, typing.Any]]: ...
    class EncryptionSettingsDecoder$(io.circe.Decoder['EncryptionSettings']):
        MODULE$: typing.ClassVar['EncryptionSettings.EncryptionSettingsDecoder.'] = ...
        def __init__(self): ...
        def accumulating(self, c: io.circe.HCursor) -> cats.data.Validated[cats.data.NonEmptyList[io.circe.DecodingFailure], 'EncryptionSettings']: ...
        def apply(self, cursor: io.circe.HCursor) -> scala.util.Either[io.circe.DecodingFailure, 'EncryptionSettings']: ...
        def at(self, field: str) -> io.circe.Decoder['EncryptionSettings']: ...
        def decodeAccumulating(self, c: io.circe.HCursor) -> cats.data.Validated[cats.data.NonEmptyList[io.circe.DecodingFailure], 'EncryptionSettings']: ...
        def decodeJson(self, j: io.circe.Json) -> scala.util.Either[io.circe.DecodingFailure, 'EncryptionSettings']: ...
        _either__B = typing.TypeVar('_either__B')  # <B>
        def either(self, decodeB: io.circe.Decoder[_either__B]) -> io.circe.Decoder[scala.util.Either['EncryptionSettings', _either__B]]: ...
        _emap__B = typing.TypeVar('_emap__B')  # <B>
        def emap(self, f: scala.Function1['EncryptionSettings', scala.util.Either[str, _emap__B]]) -> io.circe.Decoder[_emap__B]: ...
        _emapTry__B = typing.TypeVar('_emapTry__B')  # <B>
        def emapTry(self, f: scala.Function1['EncryptionSettings', scala.util.Try[_emapTry__B]]) -> io.circe.Decoder[_emapTry__B]: ...
        @typing.overload
        def ensure(self, errors: scala.Function1['EncryptionSettings', scala.collection.immutable.List[str]]) -> io.circe.Decoder['EncryptionSettings']: ...
        @typing.overload
        def ensure(self, pred: scala.Function1['EncryptionSettings', typing.Any], message: scala.Function0[str]) -> io.circe.Decoder['EncryptionSettings']: ...
        _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
        def flatMap(self, f: scala.Function1['EncryptionSettings', io.circe.Decoder[_flatMap__B]]) -> io.circe.Decoder[_flatMap__B]: ...
        def handleErrorWith(self, f: scala.Function1[io.circe.DecodingFailure, io.circe.Decoder['EncryptionSettings']]) -> io.circe.Decoder['EncryptionSettings']: ...
        def kleisli(self) -> cats.data.Kleisli[scala.util.Either, io.circe.HCursor, 'EncryptionSettings']: ...
        _map__B = typing.TypeVar('_map__B')  # <B>
        def map(self, f: scala.Function1['EncryptionSettings', _map__B]) -> io.circe.Decoder[_map__B]: ...
        def prepare(self, f: scala.Function1[io.circe.ACursor, io.circe.ACursor]) -> io.circe.Decoder['EncryptionSettings']: ...
        _product__B = typing.TypeVar('_product__B')  # <B>
        def product(self, fb: io.circe.Decoder[_product__B]) -> io.circe.Decoder[scala.Tuple2['EncryptionSettings', _product__B]]: ...
        def tryDecode(self, c: io.circe.ACursor) -> scala.util.Either[io.circe.DecodingFailure, 'EncryptionSettings']: ...
        def tryDecodeAccumulating(self, c: io.circe.ACursor) -> cats.data.Validated[cats.data.NonEmptyList[io.circe.DecodingFailure], 'EncryptionSettings']: ...
        @typing.overload
        def validate(self, errors: scala.Function1[io.circe.HCursor, scala.collection.immutable.List[str]]) -> io.circe.Decoder['EncryptionSettings']: ...
        @typing.overload
        def validate(self, pred: scala.Function1[io.circe.HCursor, typing.Any], message: scala.Function0[str]) -> io.circe.Decoder['EncryptionSettings']: ...
        def withErrorMessage(self, message: str) -> io.circe.Decoder['EncryptionSettings']: ...
    class EncryptionSettingsEncoder$(io.circe.Encoder['EncryptionSettings']):
        MODULE$: typing.ClassVar['EncryptionSettings.EncryptionSettingsEncoder.'] = ...
        def __init__(self): ...
        def apply(self, s: 'EncryptionSettings') -> io.circe.Json: ...
        _contramap__B = typing.TypeVar('_contramap__B')  # <B>
        def contramap(self, f: scala.Function1[_contramap__B, 'EncryptionSettings']) -> io.circe.Encoder[_contramap__B]: ...
        def mapJson(self, f: scala.Function1[io.circe.Json, io.circe.Json]) -> io.circe.Encoder['EncryptionSettings']: ...

class SecretStorageSettings(scala.Product, scala.Serializable):
    def __init__(self, secretDir: str, encryption: EncryptionSettings): ...
    @staticmethod
    def apply(secretDir: str, encryption: EncryptionSettings) -> 'SecretStorageSettings': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def copy(self, secretDir: str, encryption: EncryptionSettings) -> 'SecretStorageSettings': ...
    def copy$default$1(self) -> str: ...
    def copy$default$2(self) -> EncryptionSettings: ...
    @staticmethod
    def curried() -> scala.Function1[str, scala.Function1[EncryptionSettings, 'SecretStorageSettings']]: ...
    def encryption(self) -> EncryptionSettings: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def secretDir(self) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def tupled() -> scala.Function1[scala.Tuple2[str, EncryptionSettings], 'SecretStorageSettings']: ...
    @staticmethod
    def unapply(x$0: 'SecretStorageSettings') -> scala.Option[scala.Tuple2[str, EncryptionSettings]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.settings")``.

    EncryptionSettings: typing.Type[EncryptionSettings]
    SecretStorageSettings: typing.Type[SecretStorageSettings]
