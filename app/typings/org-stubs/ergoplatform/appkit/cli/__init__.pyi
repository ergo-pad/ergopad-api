import java.io
import java.lang
import org.ergoplatform.appkit
import org.ergoplatform.appkit.commands
import org.ergoplatform.appkit.config
import scala
import scala.collection
import scala.collection.immutable
import scala.runtime
import typing



class AppContext(scala.Product, scala.Serializable):
    def __init__(self, cliApp: 'CliApplication', commandLineArgs: scala.collection.Seq[str], console: 'Console', cmdOptions: scala.collection.immutable.Map[str, str], cmdName: str, cmdArgs: scala.collection.Seq[str], toolConf: org.ergoplatform.appkit.config.ErgoToolConfig, clientFactory: scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], cmdParameters: scala.collection.Seq[typing.Any]): ...
    @staticmethod
    def $lessinit$greater$default$9() -> scala.collection.Seq[typing.Any]: ...
    def apiKey(self) -> str: ...
    def apiUrl(self) -> str: ...
    @staticmethod
    def apply(cliApp: 'CliApplication', commandLineArgs: scala.collection.Seq[str], console: 'Console', cmdOptions: scala.collection.immutable.Map[str, str], cmdName: str, cmdArgs: scala.collection.Seq[str], toolConf: org.ergoplatform.appkit.config.ErgoToolConfig, clientFactory: scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], cmdParameters: scala.collection.Seq[typing.Any]) -> 'AppContext': ...
    @staticmethod
    def apply$default$9() -> scala.collection.Seq[typing.Any]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def cliApp(self) -> 'CliApplication': ...
    def clientFactory(self) -> scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient]: ...
    def cmdArgs(self) -> scala.collection.Seq[str]: ...
    def cmdName(self) -> str: ...
    def cmdOptions(self) -> scala.collection.immutable.Map[str, str]: ...
    def cmdParameters(self) -> scala.collection.Seq[typing.Any]: ...
    def commandLineArgs(self) -> scala.collection.Seq[str]: ...
    def console(self) -> 'Console': ...
    def copy(self, cliApp: 'CliApplication', commandLineArgs: scala.collection.Seq[str], console: 'Console', cmdOptions: scala.collection.immutable.Map[str, str], cmdName: str, cmdArgs: scala.collection.Seq[str], toolConf: org.ergoplatform.appkit.config.ErgoToolConfig, clientFactory: scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], cmdParameters: scala.collection.Seq[typing.Any]) -> 'AppContext': ...
    def copy$default$1(self) -> 'CliApplication': ...
    def copy$default$2(self) -> scala.collection.Seq[str]: ...
    def copy$default$3(self) -> 'Console': ...
    def copy$default$4(self) -> scala.collection.immutable.Map[str, str]: ...
    def copy$default$5(self) -> str: ...
    def copy$default$6(self) -> scala.collection.Seq[str]: ...
    def copy$default$7(self) -> org.ergoplatform.appkit.config.ErgoToolConfig: ...
    def copy$default$8(self) -> scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient]: ...
    def copy$default$9(self) -> scala.collection.Seq[typing.Any]: ...
    @staticmethod
    def curried() -> scala.Function1['CliApplication', scala.Function1[scala.collection.Seq[str], scala.Function1['Console', scala.Function1[scala.collection.immutable.Map[str, str], scala.Function1[str, scala.Function1[scala.collection.Seq[str], scala.Function1[org.ergoplatform.appkit.config.ErgoToolConfig, scala.Function1[scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], scala.Function1[scala.collection.Seq[typing.Any], 'AppContext']]]]]]]]]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def isDryRun(self) -> bool: ...
    def isPrintJson(self) -> bool: ...
    def networkType(self) -> org.ergoplatform.appkit.NetworkType: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    def toolConf(self) -> org.ergoplatform.appkit.config.ErgoToolConfig: ...
    @staticmethod
    def tupled() -> scala.Function1[scala.Tuple9['CliApplication', scala.collection.Seq[str], 'Console', scala.collection.immutable.Map[str, str], str, scala.collection.Seq[str], org.ergoplatform.appkit.config.ErgoToolConfig, scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], scala.collection.Seq[typing.Any]], 'AppContext']: ...
    @staticmethod
    def unapply(x$0: 'AppContext') -> scala.Option[scala.Tuple9['CliApplication', scala.collection.Seq[str], 'Console', scala.collection.immutable.Map[str, str], str, scala.collection.Seq[str], org.ergoplatform.appkit.config.ErgoToolConfig, scala.Function1['AppContext', org.ergoplatform.appkit.ErgoClient], scala.collection.Seq[typing.Any]]]: ...
    def withCmdParameters(self, params: scala.collection.Seq[typing.Any]) -> 'AppContext': ...

class CliApplication:
    def __init__(self): ...
    def commands(self) -> scala.collection.Seq[org.ergoplatform.appkit.commands.CmdDescriptor]: ...
    def commandsMap(self) -> scala.collection.immutable.Map[str, org.ergoplatform.appkit.commands.CmdDescriptor]: ...
    def loadConfig(self, cmdOptions: scala.collection.immutable.Map[str, str]) -> org.ergoplatform.appkit.config.ErgoToolConfig: ...
    def parseCmd(self, ctx: AppContext) -> org.ergoplatform.appkit.commands.Cmd: ...
    def printUsage(self, console: 'Console', cmdDescOpt: scala.Option[org.ergoplatform.appkit.commands.CmdDescriptor]) -> None: ...
    def run(self, args: scala.collection.Seq[str], console: 'Console', clientFactory: scala.Function1[AppContext, org.ergoplatform.appkit.ErgoClient]) -> None: ...

class CmdLineParser:
    @staticmethod
    def parseNetwork(network: str) -> org.ergoplatform.appkit.NetworkType: ...
    @staticmethod
    def parseOptions(args: scala.collection.Seq[str]) -> scala.Tuple2[scala.collection.immutable.Map[str, str], scala.collection.Seq[str]]: ...

class CmdOption(scala.Product, scala.Serializable):
    def __init__(self, name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool): ...
    @staticmethod
    def $lessinit$greater$default$4() -> bool: ...
    @staticmethod
    def Prefix() -> str: ...
    @staticmethod
    def apply(name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> 'CmdOption': ...
    @staticmethod
    def apply$default$4() -> bool: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def cmdText(self) -> str: ...
    def copy(self, name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> 'CmdOption': ...
    def copy$default$1(self) -> str: ...
    def copy$default$2(self) -> org.ergoplatform.appkit.commands.PType: ...
    def copy$default$3(self) -> str: ...
    def copy$default$4(self) -> bool: ...
    def description(self) -> str: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def helpString(self) -> str: ...
    def isFlag(self) -> bool: ...
    def name(self) -> str: ...
    @staticmethod
    def options() -> scala.collection.Seq['CmdOption']: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    def tpe(self) -> org.ergoplatform.appkit.commands.PType: ...
    @staticmethod
    def unapply(x$0: 'CmdOption') -> scala.Option[scala.Tuple4[str, org.ergoplatform.appkit.commands.PType, str, typing.Any]]: ...

class ConfigOption:
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def cmdText() -> str: ...
    @staticmethod
    def copy(name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> CmdOption: ...
    @staticmethod
    def copy$default$1() -> str: ...
    @staticmethod
    def copy$default$2() -> org.ergoplatform.appkit.commands.PType: ...
    @staticmethod
    def copy$default$3() -> str: ...
    @staticmethod
    def copy$default$4() -> bool: ...
    @staticmethod
    def description() -> str: ...
    @staticmethod
    def equals(x$1: typing.Any) -> bool: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def helpString() -> str: ...
    @staticmethod
    def isFlag() -> bool: ...
    @staticmethod
    def name() -> str: ...
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
    @staticmethod
    def tpe() -> org.ergoplatform.appkit.commands.PType: ...

class Console:
    def __init__(self): ...
    @staticmethod
    def error(msg: str) -> scala.runtime.Nothing.: ...
    @staticmethod
    def instance() -> 'Console': ...
    def println(self, s: str) -> 'Console': ...
    @typing.overload
    def readLine(self) -> str: ...
    @typing.overload
    def readLine(self, prompt: str) -> str: ...
    @typing.overload
    @staticmethod
    def readNewPassword(nAttemps: int, console: 'Console', block: scala.Function0[scala.Tuple2[org.ergoplatform.appkit.SecretString, org.ergoplatform.appkit.SecretString]]) -> org.ergoplatform.appkit.SecretString: ...
    @typing.overload
    @staticmethod
    def readNewPassword(prompt: str, secondPrompt: str, ctx: AppContext) -> org.ergoplatform.appkit.SecretString: ...
    @typing.overload
    def readPassword(self) -> org.ergoplatform.appkit.SecretString: ...
    @typing.overload
    def readPassword(self, prompt: str) -> org.ergoplatform.appkit.SecretString: ...

class ConsoleException(java.lang.RuntimeException, scala.Product, scala.Serializable):
    def __init__(self, message: str): ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    @staticmethod
    def andThen(g: scala.Function1['ConsoleException', _andThen__A]) -> scala.Function1[str, _andThen__A]: ...
    @staticmethod
    def apply(message: str) -> 'ConsoleException': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    @staticmethod
    def compose(g: scala.Function1[_compose__A, str]) -> scala.Function1[_compose__A, 'ConsoleException']: ...
    def copy(self, message: str) -> 'ConsoleException': ...
    def copy$default$1(self) -> str: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def message(self) -> str: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'ConsoleException') -> scala.Option[str]: ...

class DryRunOption:
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def cmdText() -> str: ...
    @staticmethod
    def copy(name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> CmdOption: ...
    @staticmethod
    def copy$default$1() -> str: ...
    @staticmethod
    def copy$default$2() -> org.ergoplatform.appkit.commands.PType: ...
    @staticmethod
    def copy$default$3() -> str: ...
    @staticmethod
    def copy$default$4() -> bool: ...
    @staticmethod
    def description() -> str: ...
    @staticmethod
    def equals(x$1: typing.Any) -> bool: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def helpString() -> str: ...
    @staticmethod
    def isFlag() -> bool: ...
    @staticmethod
    def name() -> str: ...
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
    @staticmethod
    def tpe() -> org.ergoplatform.appkit.commands.PType: ...

class LimitListOption:
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def cmdText() -> str: ...
    @staticmethod
    def copy(name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> CmdOption: ...
    @staticmethod
    def copy$default$1() -> str: ...
    @staticmethod
    def copy$default$2() -> org.ergoplatform.appkit.commands.PType: ...
    @staticmethod
    def copy$default$3() -> str: ...
    @staticmethod
    def copy$default$4() -> bool: ...
    @staticmethod
    def description() -> str: ...
    @staticmethod
    def equals(x$1: typing.Any) -> bool: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def helpString() -> str: ...
    @staticmethod
    def isFlag() -> bool: ...
    @staticmethod
    def name() -> str: ...
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
    @staticmethod
    def tpe() -> org.ergoplatform.appkit.commands.PType: ...

class PrintJsonOption:
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    @staticmethod
    def cmdText() -> str: ...
    @staticmethod
    def copy(name: str, tpe: org.ergoplatform.appkit.commands.PType, description: str, isFlag: bool) -> CmdOption: ...
    @staticmethod
    def copy$default$1() -> str: ...
    @staticmethod
    def copy$default$2() -> org.ergoplatform.appkit.commands.PType: ...
    @staticmethod
    def copy$default$3() -> str: ...
    @staticmethod
    def copy$default$4() -> bool: ...
    @staticmethod
    def description() -> str: ...
    @staticmethod
    def equals(x$1: typing.Any) -> bool: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def helpString() -> str: ...
    @staticmethod
    def isFlag() -> bool: ...
    @staticmethod
    def name() -> str: ...
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
    @staticmethod
    def tpe() -> org.ergoplatform.appkit.commands.PType: ...

class Utils:
    _loggedStep__T = typing.TypeVar('_loggedStep__T')  # <T>
    @staticmethod
    def loggedStep(msg: str, console: Console, step: scala.Function0[_loggedStep__T]) -> _loggedStep__T: ...

class MainConsole(Console):
    def __init__(self): ...
    def println(self, s: str) -> Console: ...
    @typing.overload
    def readLine(self) -> str: ...
    @typing.overload
    def readLine(self, prompt: str) -> str: ...
    @typing.overload
    def readPassword(self) -> org.ergoplatform.appkit.SecretString: ...
    @typing.overload
    def readPassword(self, prompt: str) -> org.ergoplatform.appkit.SecretString: ...
    def sysConsole(self) -> java.io.Console: ...

class TestConsole(Console):
    def __init__(self, in_: java.io.BufferedReader, out: java.io.PrintStream): ...
    def println(self, s: str) -> Console: ...
    @typing.overload
    def readLine(self) -> str: ...
    @typing.overload
    def readLine(self, msg: str) -> str: ...
    @typing.overload
    def readPassword(self) -> org.ergoplatform.appkit.SecretString: ...
    @typing.overload
    def readPassword(self, msg: str) -> org.ergoplatform.appkit.SecretString: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.appkit.cli")``.

    AppContext: typing.Type[AppContext]
    CliApplication: typing.Type[CliApplication]
    CmdLineParser: typing.Type[CmdLineParser]
    CmdOption: typing.Type[CmdOption]
    ConfigOption: typing.Type[ConfigOption]
    Console: typing.Type[Console]
    ConsoleException: typing.Type[ConsoleException]
    DryRunOption: typing.Type[DryRunOption]
    LimitListOption: typing.Type[LimitListOption]
    MainConsole: typing.Type[MainConsole]
    PrintJsonOption: typing.Type[PrintJsonOption]
    TestConsole: typing.Type[TestConsole]
    Utils: typing.Type[Utils]
