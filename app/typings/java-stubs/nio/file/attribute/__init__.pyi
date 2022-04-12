import java.io
import java.lang
import java.nio
import java.security
import java.time
import java.util
import java.util.concurrent
import typing



class AclEntry:
    def equals(self, object: typing.Any) -> bool: ...
    def flags(self) -> java.util.Set['AclEntryFlag']: ...
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def newBuilder() -> 'AclEntry.Builder': ...
    @typing.overload
    @staticmethod
    def newBuilder(aclEntry: 'AclEntry') -> 'AclEntry.Builder': ...
    def permissions(self) -> java.util.Set['AclEntryPermission']: ...
    def principal(self) -> 'UserPrincipal': ...
    def toString(self) -> str: ...
    def type(self) -> 'AclEntryType': ...
    class Builder:
        def build(self) -> 'AclEntry': ...
        @typing.overload
        def setFlags(self, aclEntryFlagArray: typing.List['AclEntryFlag']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setFlags(self, set: java.util.Set['AclEntryFlag']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setPermissions(self, aclEntryPermissionArray: typing.List['AclEntryPermission']) -> 'AclEntry.Builder': ...
        @typing.overload
        def setPermissions(self, set: java.util.Set['AclEntryPermission']) -> 'AclEntry.Builder': ...
        def setPrincipal(self, userPrincipal: 'UserPrincipal') -> 'AclEntry.Builder': ...
        def setType(self, aclEntryType: 'AclEntryType') -> 'AclEntry.Builder': ...

class AclEntryFlag(java.lang.Enum['AclEntryFlag']):
    FILE_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    DIRECTORY_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    NO_PROPAGATE_INHERIT: typing.ClassVar['AclEntryFlag'] = ...
    INHERIT_ONLY: typing.ClassVar['AclEntryFlag'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AclEntryFlag': ...
    @staticmethod
    def values() -> typing.List['AclEntryFlag']: ...

class AclEntryPermission(java.lang.Enum['AclEntryPermission']):
    READ_DATA: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_DATA: typing.ClassVar['AclEntryPermission'] = ...
    APPEND_DATA: typing.ClassVar['AclEntryPermission'] = ...
    READ_NAMED_ATTRS: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_NAMED_ATTRS: typing.ClassVar['AclEntryPermission'] = ...
    EXECUTE: typing.ClassVar['AclEntryPermission'] = ...
    DELETE_CHILD: typing.ClassVar['AclEntryPermission'] = ...
    READ_ATTRIBUTES: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_ATTRIBUTES: typing.ClassVar['AclEntryPermission'] = ...
    DELETE: typing.ClassVar['AclEntryPermission'] = ...
    READ_ACL: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_ACL: typing.ClassVar['AclEntryPermission'] = ...
    WRITE_OWNER: typing.ClassVar['AclEntryPermission'] = ...
    SYNCHRONIZE: typing.ClassVar['AclEntryPermission'] = ...
    LIST_DIRECTORY: typing.ClassVar['AclEntryPermission'] = ...
    ADD_FILE: typing.ClassVar['AclEntryPermission'] = ...
    ADD_SUBDIRECTORY: typing.ClassVar['AclEntryPermission'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AclEntryPermission': ...
    @staticmethod
    def values() -> typing.List['AclEntryPermission']: ...

class AclEntryType(java.lang.Enum['AclEntryType']):
    ALLOW: typing.ClassVar['AclEntryType'] = ...
    DENY: typing.ClassVar['AclEntryType'] = ...
    AUDIT: typing.ClassVar['AclEntryType'] = ...
    ALARM: typing.ClassVar['AclEntryType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AclEntryType': ...
    @staticmethod
    def values() -> typing.List['AclEntryType']: ...

class AttributeView:
    def name(self) -> str: ...

class BasicFileAttributes:
    def creationTime(self) -> 'FileTime': ...
    def fileKey(self) -> typing.Any: ...
    def isDirectory(self) -> bool: ...
    def isOther(self) -> bool: ...
    def isRegularFile(self) -> bool: ...
    def isSymbolicLink(self) -> bool: ...
    def lastAccessTime(self) -> 'FileTime': ...
    def lastModifiedTime(self) -> 'FileTime': ...
    def size(self) -> int: ...

_FileAttribute__T = typing.TypeVar('_FileAttribute__T')  # <T>
class FileAttribute(typing.Generic[_FileAttribute__T]):
    def name(self) -> str: ...
    def value(self) -> _FileAttribute__T: ...

class FileTime(java.lang.Comparable['FileTime']):
    def compareTo(self, fileTime: 'FileTime') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def fromMillis(long: int) -> 'FileTime': ...
    def hashCode(self) -> int: ...
    def to(self, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def toInstant(self) -> java.time.Instant: ...
    def toMillis(self) -> int: ...
    def toString(self) -> str: ...

class PosixFilePermission(java.lang.Enum['PosixFilePermission']):
    OWNER_READ: typing.ClassVar['PosixFilePermission'] = ...
    OWNER_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    OWNER_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_READ: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    GROUP_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_READ: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_WRITE: typing.ClassVar['PosixFilePermission'] = ...
    OTHERS_EXECUTE: typing.ClassVar['PosixFilePermission'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PosixFilePermission': ...
    @staticmethod
    def values() -> typing.List['PosixFilePermission']: ...

class PosixFilePermissions:
    @staticmethod
    def asFileAttribute(set: java.util.Set[PosixFilePermission]) -> FileAttribute[java.util.Set[PosixFilePermission]]: ...
    @staticmethod
    def fromString(string: str) -> java.util.Set[PosixFilePermission]: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(set: java.util.Set[PosixFilePermission]) -> str: ...

class UserPrincipal(java.security.Principal):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class UserPrincipalLookupService:
    def lookupPrincipalByGroupName(self, string: str) -> 'GroupPrincipal': ...
    def lookupPrincipalByName(self, string: str) -> UserPrincipal: ...

class UserPrincipalNotFoundException(java.io.IOException):
    def __init__(self, string: str): ...
    def getName(self) -> str: ...

class DosFileAttributes(BasicFileAttributes):
    def isArchive(self) -> bool: ...
    def isHidden(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isSystem(self) -> bool: ...

class FileAttributeView(AttributeView): ...

class FileStoreAttributeView(AttributeView): ...

class GroupPrincipal(UserPrincipal):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class PosixFileAttributes(BasicFileAttributes):
    def group(self) -> GroupPrincipal: ...
    def owner(self) -> UserPrincipal: ...
    def permissions(self) -> java.util.Set[PosixFilePermission]: ...

class BasicFileAttributeView(FileAttributeView):
    def name(self) -> str: ...
    def readAttributes(self) -> BasicFileAttributes: ...
    def setTimes(self, fileTime: FileTime, fileTime2: FileTime, fileTime3: FileTime) -> None: ...

class FileOwnerAttributeView(FileAttributeView):
    def getOwner(self) -> UserPrincipal: ...
    def name(self) -> str: ...
    def setOwner(self, userPrincipal: UserPrincipal) -> None: ...

class UserDefinedFileAttributeView(FileAttributeView):
    def delete(self, string: str) -> None: ...
    def list(self) -> java.util.List[str]: ...
    def name(self) -> str: ...
    def read(self, string: str, byteBuffer: java.nio.ByteBuffer) -> int: ...
    def size(self, string: str) -> int: ...
    def write(self, string: str, byteBuffer: java.nio.ByteBuffer) -> int: ...

class AclFileAttributeView(FileOwnerAttributeView):
    def getAcl(self) -> java.util.List[AclEntry]: ...
    def name(self) -> str: ...
    def setAcl(self, list: java.util.List[AclEntry]) -> None: ...

class DosFileAttributeView(BasicFileAttributeView):
    def name(self) -> str: ...
    def readAttributes(self) -> DosFileAttributes: ...
    def setArchive(self, boolean: bool) -> None: ...
    def setHidden(self, boolean: bool) -> None: ...
    def setReadOnly(self, boolean: bool) -> None: ...
    def setSystem(self, boolean: bool) -> None: ...

class PosixFileAttributeView(BasicFileAttributeView, FileOwnerAttributeView):
    def name(self) -> str: ...
    def readAttributes(self) -> PosixFileAttributes: ...
    def setGroup(self, groupPrincipal: GroupPrincipal) -> None: ...
    def setPermissions(self, set: java.util.Set[PosixFilePermission]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.file.attribute")``.

    AclEntry: typing.Type[AclEntry]
    AclEntryFlag: typing.Type[AclEntryFlag]
    AclEntryPermission: typing.Type[AclEntryPermission]
    AclEntryType: typing.Type[AclEntryType]
    AclFileAttributeView: typing.Type[AclFileAttributeView]
    AttributeView: typing.Type[AttributeView]
    BasicFileAttributeView: typing.Type[BasicFileAttributeView]
    BasicFileAttributes: typing.Type[BasicFileAttributes]
    DosFileAttributeView: typing.Type[DosFileAttributeView]
    DosFileAttributes: typing.Type[DosFileAttributes]
    FileAttribute: typing.Type[FileAttribute]
    FileAttributeView: typing.Type[FileAttributeView]
    FileOwnerAttributeView: typing.Type[FileOwnerAttributeView]
    FileStoreAttributeView: typing.Type[FileStoreAttributeView]
    FileTime: typing.Type[FileTime]
    GroupPrincipal: typing.Type[GroupPrincipal]
    PosixFileAttributeView: typing.Type[PosixFileAttributeView]
    PosixFileAttributes: typing.Type[PosixFileAttributes]
    PosixFilePermission: typing.Type[PosixFilePermission]
    PosixFilePermissions: typing.Type[PosixFilePermissions]
    UserDefinedFileAttributeView: typing.Type[UserDefinedFileAttributeView]
    UserPrincipal: typing.Type[UserPrincipal]
    UserPrincipalLookupService: typing.Type[UserPrincipalLookupService]
    UserPrincipalNotFoundException: typing.Type[UserPrincipalNotFoundException]
