import org
import org.ergoplatform
import scala
import scala.collection
import scala.collection.immutable
import scala.runtime
import scala.util
import scalan
import scorex.crypto.authds.avltree.batch
import scorex.crypto.hash
import sigmastate
import sigmastate.eval
import sigmastate.interpreter
import special.collection
import special.sigma
import typing



class AvlTreeHelpers:
    @staticmethod
    def createAvlTree(flags: sigmastate.AvlTreeFlags, entries: scala.collection.Seq[scala.Tuple2[typing.List[int], typing.List[int]]]) -> scala.Tuple2[special.sigma.AvlTree, scorex.crypto.authds.avltree.batch.BatchAVLProver[typing.List[int], scorex.crypto.hash.Blake2b256.]]: ...
    class ADKeyArrayOps:
        def __init__(self, arr: typing.List[typing.List[int]]): ...
        def toColl(self) -> special.collection.Coll[special.collection.Coll[typing.Any]]: ...
    class ADKeyValueArrayOps:
        def __init__(self, arr: typing.List[scala.Tuple2[typing.List[int], typing.List[int]]]): ...
        def toColl(self) -> special.collection.Coll[scala.Tuple2[special.collection.Coll[typing.Any], special.collection.Coll[typing.Any]]]: ...

class ContractSyntax:
    @staticmethod
    def $init$($this: 'ContractSyntax') -> None: ...
    _Coll__T = typing.TypeVar('_Coll__T')  # <T>
    def Coll(self, items: scala.collection.Seq[_Coll__T], cT: scalan.RType[_Coll__T]) -> special.collection.Coll[_Coll__T]: ...
    def Env(self, entries: scala.collection.Seq[scala.Tuple2[str, typing.Any]]) -> scala.collection.immutable.Map[str, typing.Any]: ...
    def builder(self) -> special.sigma.SigmaDslBuilder: ...
    def contractEnv(self) -> scala.collection.immutable.Map[str, typing.Any]: ...
    def org$ergoplatform$dsl$ContractSyntax$_setter_$syntax_$eq(self, x$1: special.sigma.DslSyntaxExtensions) -> None: ...
    def proposition(self, name: str, dslSpec: scala.Function1[special.sigma.Context, special.sigma.SigmaProp], scriptCode: str, scriptVersion: scala.Option[typing.Any]) -> 'ContractSpec.PropositionSpec': ...
    def proposition$default$4(self) -> scala.Option[typing.Any]: ...
    def spec(self) -> 'ContractSpec': ...
    def syntax(self) -> special.sigma.DslSyntaxExtensions: ...
    def verifier(self) -> 'ContractSpec.VerifyingParty': ...
    class ErgoScript(scala.Product, scala.Serializable):
        def __init__(self, env: scala.collection.immutable.Map[str, typing.Any], code: str, scriptVersion: scala.Option[typing.Any]): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def code(self) -> str: ...
        def copy(self, env: scala.collection.immutable.Map[str, typing.Any], code: str, scriptVersion: scala.Option[typing.Any]) -> 'ContractSyntax.ErgoScript': ...
        def copy$default$1(self) -> scala.collection.immutable.Map[str, typing.Any]: ...
        def copy$default$2(self) -> str: ...
        def copy$default$3(self) -> scala.Option[typing.Any]: ...
        def env(self) -> scala.collection.immutable.Map[str, typing.Any]: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> str: ...
        def scriptVersion(self) -> scala.Option[typing.Any]: ...
        def toString(self) -> str: ...
    class ErgoScript$(scala.runtime.AbstractFunction3[scala.collection.immutable.Map[str, typing.Any], str, scala.Option[typing.Any], 'ContractSyntax.ErgoScript'], scala.Serializable):
        MODULE$: typing.ClassVar['ContractSyntax.ErgoScript.'] = ...
        def __init__(self): ...
        def apply(self, env: scala.collection.immutable.Map[str, typing.Any], code: str, scriptVersion: scala.Option[typing.Any]) -> 'ContractSyntax.ErgoScript': ...
        def toString(self) -> str: ...
        def unapply(self, x$0: 'ContractSyntax.ErgoScript') -> scala.Option[scala.Tuple3[scala.collection.immutable.Map[str, typing.Any], str, scala.Option[typing.Any]]]: ...
    class Token(scala.Product, scala.Serializable):
        def __init__(self, id: special.collection.Coll[typing.Any], value: int): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, id: special.collection.Coll[typing.Any], value: int) -> 'ContractSyntax.Token': ...
        def copy$default$1(self) -> special.collection.Coll[typing.Any]: ...
        def copy$default$2(self) -> int: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def id(self) -> special.collection.Coll[typing.Any]: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> str: ...
        def toString(self) -> str: ...
        def value(self) -> int: ...
    class Token$(scala.runtime.AbstractFunction2[special.collection.Coll[typing.Any], typing.Any, 'ContractSyntax.Token'], scala.Serializable):
        MODULE$: typing.ClassVar['ContractSyntax.Token.'] = ...
        def __init__(self): ...
        def apply(self, id: special.collection.Coll[typing.Any], value: int) -> 'ContractSyntax.Token': ...
        def toString(self) -> str: ...
        def unapply(self, x$0: 'ContractSyntax.Token') -> scala.Option[scala.Tuple2[special.collection.Coll[typing.Any], typing.Any]]: ...

class StdContracts:
    @staticmethod
    def $init$($this: 'StdContracts') -> None: ...
    def transferErgWithChange(self, tx: 'ContractSpec.TransactionCandidate', from_: 'ContractSpec.OutBox', to: 'ContractSpec.PropositionSpec', ergAmt: int) -> scala.Tuple2['ContractSpec.OutBox', scala.Option['ContractSpec.OutBox']]: ...
    def transferTokenWithChange(self, tx: 'ContractSpec.TransactionCandidate', from_: 'ContractSpec.OutBox', to: 'ContractSpec.PropositionSpec', tokenAmt: ContractSyntax.Token) -> scala.Tuple2['ContractSpec.OutBox', scala.Option['ContractSpec.OutBox']]: ...

class SigmaContractSyntax(special.sigma.SigmaContract, ContractSyntax): ...

class ContractSpec:
    @staticmethod
    def $init$($this: 'ContractSpec') -> None: ...
    _Coll__T = typing.TypeVar('_Coll__T')  # <T>
    def Coll(self, items: typing.Any, cT: scalan.RType[_Coll__T]) -> special.collection.Coll[_Coll__T]: ...
    def Colls(self) -> special.collection.CollBuilder: ...
    def IR(self) -> sigmastate.eval.IRContext: ...
    def MinErgValue(self) -> int: ...
    def dsl(self) -> special.sigma.SigmaDslBuilder: ...
    def error(self, msg: str) -> scala.runtime.Nothing.: ...
    def mkPropositionSpec(self, name: str, dslSpec: scala.Function1[special.sigma.Context, special.sigma.SigmaProp], scriptSpec: ContractSyntax.ErgoScript) -> 'ContractSpec.PropositionSpec': ...
    def mkProvingParty(self, name: str) -> 'ContractSpec.ProvingParty': ...
    def mkVerifyingParty(self, name: str) -> 'ContractSpec.VerifyingParty': ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$Colls_$eq(self, x$1: special.collection.CollBuilder) -> None: ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$MinErgValue_$eq(self, x$1: int) -> None: ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$dsl_$eq(self, x$1: special.sigma.SigmaDslBuilder) -> None: ...
    class BlockCandidate:
        def height(self) -> int: ...
        def newTransaction(self) -> 'ContractSpec.TransactionCandidate': ...
    class ChainBlock:
        def getTransactions(self) -> scala.collection.Seq['ContractSpec.ChainTransaction']: ...
    class ChainTransaction:
        def outputs(self) -> scala.collection.Seq['ContractSpec.OutBox']: ...
    class InputBox:
        def runDsl(self, extensions: scala.collection.immutable.Map[typing.Any, special.sigma.AnyValue]) -> special.sigma.SigmaProp: ...
        def runDsl$default$1(self) -> scala.collection.immutable.Map[typing.Any, special.sigma.AnyValue]: ...
        def toErgoContext(self) -> org.ergoplatform.ErgoLikeContext: ...
        def tx(self) -> 'ContractSpec.TransactionCandidate': ...
        def utxoBox(self) -> 'ContractSpec.OutBox': ...
    class OutBox:
        def boxIndex(self) -> int: ...
        def ergoBox(self) -> org.ergoplatform.ErgoBox: ...
        def id(self) -> typing.List[int]: ...
        def propSpec(self) -> 'ContractSpec.PropositionSpec': ...
        def token(self, id: special.collection.Coll[typing.Any]) -> ContractSyntax.Token: ...
        def tx(self) -> 'ContractSpec.TransactionCandidate': ...
        def value(self) -> int: ...
        def withRegs(self, regs: scala.collection.Seq[scala.Tuple2[org.ergoplatform.ErgoBox.NonMandatoryRegisterId, typing.Any]]) -> 'ContractSpec.OutBox': ...
        def withTokens(self, tokens: scala.collection.Seq[ContractSyntax.Token]) -> 'ContractSpec.OutBox': ...
    class PropositionSpec:
        def dslSpec(self) -> scala.Function1[special.sigma.Context, special.sigma.SigmaProp]: ...
        def ergoTree(self) -> sigmastate.Values.ErgoTree: ...
        def name(self) -> str: ...
        def scriptSpec(self) -> ContractSyntax.ErgoScript: ...
    class PropositionSpec$:
        def __init__(self, $outer: 'ContractSpec'): ...
        def apply(self, name: str, dslSpec: scala.Function1[special.sigma.Context, special.sigma.SigmaProp], scriptSpec: ContractSyntax.ErgoScript) -> 'ContractSpec.PropositionSpec': ...
    class ProtocolParty:
        def name(self) -> str: ...
    class ProvingParty(org.ergoplatform.dsl.ContractSpec.ProtocolParty):
        def prove(self, inBox: 'ContractSpec.InputBox', extensions: scala.collection.immutable.Map[typing.Any, special.sigma.AnyValue]) -> scala.util.Try[sigmastate.interpreter.CostedProverResult]: ...
        def prove$default$2(self) -> scala.collection.immutable.Map[typing.Any, special.sigma.AnyValue]: ...
        def pubKey(self) -> special.sigma.SigmaProp: ...
    class ProvingParty$:
        def __init__(self, $outer: 'ContractSpec'): ...
        def apply(self, name: str) -> 'ContractSpec.ProvingParty': ...
    class TransactionCandidate:
        def block(self) -> 'ContractSpec.BlockCandidate': ...
        def dataInputs(self) -> scala.collection.Seq['ContractSpec.InputBox']: ...
        def inBox(self, utxoBox: 'ContractSpec.OutBox') -> 'ContractSpec.InputBox': ...
        def inputs(self) -> scala.collection.Seq['ContractSpec.InputBox']: ...
        def outBox(self, value: int, propSpec: 'ContractSpec.PropositionSpec') -> 'ContractSpec.OutBox': ...
        def outputs(self) -> scala.collection.Seq['ContractSpec.OutBox']: ...
        def spending(self, utxos: scala.collection.Seq['ContractSpec.OutBox']) -> 'ContractSpec.TransactionCandidate': ...
        def withDataInputs(self, dataBoxes: scala.collection.Seq['ContractSpec.OutBox']) -> 'ContractSpec.TransactionCandidate': ...
    class VerifyingParty(org.ergoplatform.dsl.ContractSpec.ProtocolParty):
        def verify(self, inBox: 'ContractSpec.InputBox', proverResult: sigmastate.interpreter.ProverResult) -> bool: ...
    class VerifyingParty$:
        def __init__(self, $outer: 'ContractSpec'): ...
        def apply(self, name: str) -> 'ContractSpec.VerifyingParty': ...

class ErgoContractSpec(ContractSpec):
    def __init__(self, IR: sigmastate.eval.IRContext): ...
    _Coll__T = typing.TypeVar('_Coll__T')  # <T>
    def Coll(self, items: typing.Any, cT: scalan.RType[_Coll__T]) -> special.collection.Coll[_Coll__T]: ...
    def Colls(self) -> special.collection.CollBuilder: ...
    def IR(self) -> sigmastate.eval.IRContext: ...
    def MinErgValue(self) -> int: ...
    def PropositionSpec(self) -> ContractSpec.PropositionSpec.: ...
    def ProvingParty(self) -> ContractSpec.ProvingParty.: ...
    def VerifyingParty(self) -> ContractSpec.VerifyingParty.: ...
    def dsl(self) -> special.sigma.SigmaDslBuilder: ...
    def error(self, msg: str) -> scala.runtime.Nothing.: ...
    def getBlock(self, height: int) -> ContractSpec.ChainBlock: ...
    def getBoxById(self, id: special.collection.Coll[typing.Any]) -> ContractSpec.OutBox: ...
    def getBoxesByParty(self, party: ContractSpec.ProtocolParty) -> scala.collection.Seq[ContractSpec.OutBox]: ...
    def mkPropositionSpec(self, name: str, dslSpec: scala.Function1[special.sigma.Context, special.sigma.SigmaProp], scriptSpec: ContractSyntax.ErgoScript) -> scala.runtime.Nothing.: ...
    def mkProvingParty(self, name: str) -> ContractSpec.ProvingParty: ...
    def mkVerifyingParty(self, name: str) -> ContractSpec.VerifyingParty: ...
    def newTransactionContext(self) -> 'ErgoContractSpec.TransactionContext': ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$Colls_$eq(self, x$1: special.collection.CollBuilder) -> None: ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$MinErgValue_$eq(self, x$1: int) -> None: ...
    def org$ergoplatform$dsl$ContractSpec$_setter_$dsl_$eq(self, x$1: special.sigma.SigmaDslBuilder) -> None: ...
    class ErgoOutBox(ContractSpec.OutBox, scala.Product, scala.Serializable):
        $outer: 'ErgoContractSpec' = ...
        def __init__(self, $outer: 'ErgoContractSpec', tx: ContractSpec.TransactionCandidate, boxIndex: int, value: int, propSpec: ContractSpec.PropositionSpec): ...
        def boxIndex(self) -> int: ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, tx: ContractSpec.TransactionCandidate, boxIndex: int, value: int, propSpec: ContractSpec.PropositionSpec) -> 'ErgoContractSpec.ErgoOutBox': ...
        def copy$default$1(self) -> ContractSpec.TransactionCandidate: ...
        def copy$default$2(self) -> int: ...
        def copy$default$3(self) -> int: ...
        def copy$default$4(self) -> ContractSpec.PropositionSpec: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def ergoBox(self) -> scala.runtime.Nothing.: ...
        def hashCode(self) -> int: ...
        def id(self) -> typing.List[int]: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> str: ...
        def propSpec(self) -> ContractSpec.PropositionSpec: ...
        def toString(self) -> str: ...
        def token(self, id: special.collection.Coll[typing.Any]) -> ContractSyntax.Token: ...
        def tx(self) -> ContractSpec.TransactionCandidate: ...
        def value(self) -> int: ...
        def withRegs(self, regs: scala.collection.Seq[scala.Tuple2[org.ergoplatform.ErgoBox.NonMandatoryRegisterId, typing.Any]]) -> ContractSpec.OutBox: ...
        def withTokens(self, tokens: scala.collection.Seq[ContractSyntax.Token]) -> ContractSpec.OutBox: ...
    class ErgoOutBox$(scala.runtime.AbstractFunction4[ContractSpec.TransactionCandidate, typing.Any, typing.Any, ContractSpec.PropositionSpec, 'ErgoContractSpec.ErgoOutBox'], scala.Serializable):
        def __init__(self, $outer: 'ErgoContractSpec'): ...
        def apply(self, tx: ContractSpec.TransactionCandidate, boxIndex: int, value: int, propSpec: ContractSpec.PropositionSpec) -> 'ErgoContractSpec.ErgoOutBox': ...
        def toString(self) -> str: ...
        def unapply(self, x$0: 'ErgoContractSpec.ErgoOutBox') -> scala.Option[scala.Tuple4[ContractSpec.TransactionCandidate, typing.Any, typing.Any, ContractSpec.PropositionSpec]]: ...
    class TransactionContext:
        def attachProof(self, proofs: scala.collection.Seq[scala.Tuple2[ContractSpec.InputBox, sigmastate.interpreter.CostedProverResult]]) -> None: ...
        def block(self) -> ContractSpec.BlockCandidate: ...
        def submit(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.dsl")``.

    AvlTreeHelpers: typing.Type[AvlTreeHelpers]
    ContractSpec: typing.Type[ContractSpec]
    ContractSyntax: typing.Type[ContractSyntax]
    ErgoContractSpec: typing.Type[ErgoContractSpec]
    SigmaContractSyntax: typing.Type[SigmaContractSyntax]
    StdContracts: typing.Type[StdContracts]
