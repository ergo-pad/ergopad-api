import java
import java.io
import java.lang
import java.util.function
import typing



class AtomicBoolean(java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def compareAndExchange(self, boolean: bool, boolean2: bool) -> bool: ...
    def compareAndExchangeAcquire(self, boolean: bool, boolean2: bool) -> bool: ...
    def compareAndExchangeRelease(self, boolean: bool, boolean2: bool) -> bool: ...
    def compareAndSet(self, boolean: bool, boolean2: bool) -> bool: ...
    def get(self) -> bool: ...
    def getAcquire(self) -> bool: ...
    def getAndSet(self, boolean: bool) -> bool: ...
    def getOpaque(self) -> bool: ...
    def getPlain(self) -> bool: ...
    def lazySet(self, boolean: bool) -> None: ...
    def set(self, boolean: bool) -> None: ...
    def setOpaque(self, boolean: bool) -> None: ...
    def setPlain(self, boolean: bool) -> None: ...
    def setRelease(self, boolean: bool) -> None: ...
    def toString(self) -> str: ...
    def weakCompareAndSet(self, boolean: bool, boolean2: bool) -> bool: ...
    def weakCompareAndSetAcquire(self, boolean: bool, boolean2: bool) -> bool: ...
    def weakCompareAndSetPlain(self, boolean: bool, boolean2: bool) -> bool: ...
    def weakCompareAndSetRelease(self, boolean: bool, boolean2: bool) -> bool: ...
    def weakCompareAndSetVolatile(self, boolean: bool, boolean2: bool) -> bool: ...

class AtomicInteger(java.lang.Number, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def accumulateAndGet(self, int: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, int: int) -> int: ...
    def compareAndExchange(self, int: int, int2: int) -> int: ...
    def compareAndExchangeAcquire(self, int: int, int2: int) -> int: ...
    def compareAndExchangeRelease(self, int: int, int2: int) -> int: ...
    def compareAndSet(self, int: int, int2: int) -> bool: ...
    def decrementAndGet(self) -> int: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def get(self) -> int: ...
    def getAcquire(self) -> int: ...
    def getAndAccumulate(self, int: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, int: int) -> int: ...
    def getAndDecrement(self) -> int: ...
    def getAndIncrement(self) -> int: ...
    def getAndSet(self, int: int) -> int: ...
    def getAndUpdate(self, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def getOpaque(self) -> int: ...
    def getPlain(self) -> int: ...
    def incrementAndGet(self) -> int: ...
    def intValue(self) -> int: ...
    def lazySet(self, int: int) -> None: ...
    def longValue(self) -> int: ...
    def set(self, int: int) -> None: ...
    def setOpaque(self, int: int) -> None: ...
    def setPlain(self, int: int) -> None: ...
    def setRelease(self, int: int) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, int: int, int2: int) -> bool: ...
    def weakCompareAndSetAcquire(self, int: int, int2: int) -> bool: ...
    def weakCompareAndSetPlain(self, int: int, int2: int) -> bool: ...
    def weakCompareAndSetRelease(self, int: int, int2: int) -> bool: ...
    def weakCompareAndSetVolatile(self, int: int, int2: int) -> bool: ...

class AtomicIntegerArray(java.io.Serializable):
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, intArray: typing.List[int]): ...
    def accumulateAndGet(self, int: int, int2: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, int: int, int2: int) -> int: ...
    def compareAndExchange(self, int: int, int2: int, int3: int) -> int: ...
    def compareAndExchangeAcquire(self, int: int, int2: int, int3: int) -> int: ...
    def compareAndExchangeRelease(self, int: int, int2: int, int3: int) -> int: ...
    def compareAndSet(self, int: int, int2: int, int3: int) -> bool: ...
    def decrementAndGet(self, int: int) -> int: ...
    def get(self, int: int) -> int: ...
    def getAcquire(self, int: int) -> int: ...
    def getAndAccumulate(self, int: int, int2: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, int: int, int2: int) -> int: ...
    def getAndDecrement(self, int: int) -> int: ...
    def getAndIncrement(self, int: int) -> int: ...
    def getAndSet(self, int: int, int2: int) -> int: ...
    def getAndUpdate(self, int: int, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def getOpaque(self, int: int) -> int: ...
    def getPlain(self, int: int) -> int: ...
    def incrementAndGet(self, int: int) -> int: ...
    def lazySet(self, int: int, int2: int) -> None: ...
    def length(self) -> int: ...
    def set(self, int: int, int2: int) -> None: ...
    def setOpaque(self, int: int, int2: int) -> None: ...
    def setPlain(self, int: int, int2: int) -> None: ...
    def setRelease(self, int: int, int2: int) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, int: int, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, int: int, int2: int, int3: int) -> bool: ...
    def weakCompareAndSetAcquire(self, int: int, int2: int, int3: int) -> bool: ...
    def weakCompareAndSetPlain(self, int: int, int2: int, int3: int) -> bool: ...
    def weakCompareAndSetRelease(self, int: int, int2: int, int3: int) -> bool: ...
    def weakCompareAndSetVolatile(self, int: int, int2: int, int3: int) -> bool: ...

_AtomicIntegerFieldUpdater__T = typing.TypeVar('_AtomicIntegerFieldUpdater__T')  # <T>
class AtomicIntegerFieldUpdater(typing.Generic[_AtomicIntegerFieldUpdater__T]):
    def accumulateAndGet(self, t: _AtomicIntegerFieldUpdater__T, int: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, t: _AtomicIntegerFieldUpdater__T, int: int) -> int: ...
    def compareAndSet(self, t: _AtomicIntegerFieldUpdater__T, int: int, int2: int) -> bool: ...
    def decrementAndGet(self, t: _AtomicIntegerFieldUpdater__T) -> int: ...
    def get(self, t: _AtomicIntegerFieldUpdater__T) -> int: ...
    def getAndAccumulate(self, t: _AtomicIntegerFieldUpdater__T, int: int, intBinaryOperator: typing.Union[java.util.function.IntBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, t: _AtomicIntegerFieldUpdater__T, int: int) -> int: ...
    def getAndDecrement(self, t: _AtomicIntegerFieldUpdater__T) -> int: ...
    def getAndIncrement(self, t: _AtomicIntegerFieldUpdater__T) -> int: ...
    def getAndSet(self, t: _AtomicIntegerFieldUpdater__T, int: int) -> int: ...
    def getAndUpdate(self, t: _AtomicIntegerFieldUpdater__T, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def incrementAndGet(self, t: _AtomicIntegerFieldUpdater__T) -> int: ...
    def lazySet(self, t: _AtomicIntegerFieldUpdater__T, int: int) -> None: ...
    _newUpdater__U = typing.TypeVar('_newUpdater__U')  # <U>
    @staticmethod
    def newUpdater(class_: typing.Type[_newUpdater__U], string: str) -> 'AtomicIntegerFieldUpdater'[_newUpdater__U]: ...
    def set(self, t: _AtomicIntegerFieldUpdater__T, int: int) -> None: ...
    def updateAndGet(self, t: _AtomicIntegerFieldUpdater__T, intUnaryOperator: typing.Union[java.util.function.IntUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, t: _AtomicIntegerFieldUpdater__T, int: int, int2: int) -> bool: ...

class AtomicLong(java.lang.Number, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    def accumulateAndGet(self, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, long: int) -> int: ...
    def compareAndExchange(self, long: int, long2: int) -> int: ...
    def compareAndExchangeAcquire(self, long: int, long2: int) -> int: ...
    def compareAndExchangeRelease(self, long: int, long2: int) -> int: ...
    def compareAndSet(self, long: int, long2: int) -> bool: ...
    def decrementAndGet(self) -> int: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def get(self) -> int: ...
    def getAcquire(self) -> int: ...
    def getAndAccumulate(self, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, long: int) -> int: ...
    def getAndDecrement(self) -> int: ...
    def getAndIncrement(self) -> int: ...
    def getAndSet(self, long: int) -> int: ...
    def getAndUpdate(self, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def getOpaque(self) -> int: ...
    def getPlain(self) -> int: ...
    def incrementAndGet(self) -> int: ...
    def intValue(self) -> int: ...
    def lazySet(self, long: int) -> None: ...
    def longValue(self) -> int: ...
    def set(self, long: int) -> None: ...
    def setOpaque(self, long: int) -> None: ...
    def setPlain(self, long: int) -> None: ...
    def setRelease(self, long: int) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, long: int, long2: int) -> bool: ...
    def weakCompareAndSetAcquire(self, long: int, long2: int) -> bool: ...
    def weakCompareAndSetPlain(self, long: int, long2: int) -> bool: ...
    def weakCompareAndSetRelease(self, long: int, long2: int) -> bool: ...
    def weakCompareAndSetVolatile(self, long: int, long2: int) -> bool: ...

class AtomicLongArray(java.io.Serializable):
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, longArray: typing.List[int]): ...
    def accumulateAndGet(self, int: int, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, int: int, long: int) -> int: ...
    def compareAndExchange(self, int: int, long: int, long2: int) -> int: ...
    def compareAndExchangeAcquire(self, int: int, long: int, long2: int) -> int: ...
    def compareAndExchangeRelease(self, int: int, long: int, long2: int) -> int: ...
    def compareAndSet(self, int: int, long: int, long2: int) -> bool: ...
    def decrementAndGet(self, int: int) -> int: ...
    def get(self, int: int) -> int: ...
    def getAcquire(self, int: int) -> int: ...
    def getAndAccumulate(self, int: int, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, int: int, long: int) -> int: ...
    def getAndDecrement(self, int: int) -> int: ...
    def getAndIncrement(self, int: int) -> int: ...
    def getAndSet(self, int: int, long: int) -> int: ...
    def getAndUpdate(self, int: int, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def getOpaque(self, int: int) -> int: ...
    def getPlain(self, int: int) -> int: ...
    def incrementAndGet(self, int: int) -> int: ...
    def lazySet(self, int: int, long: int) -> None: ...
    def length(self) -> int: ...
    def set(self, int: int, long: int) -> None: ...
    def setOpaque(self, int: int, long: int) -> None: ...
    def setPlain(self, int: int, long: int) -> None: ...
    def setRelease(self, int: int, long: int) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, int: int, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, int: int, long: int, long2: int) -> bool: ...
    def weakCompareAndSetAcquire(self, int: int, long: int, long2: int) -> bool: ...
    def weakCompareAndSetPlain(self, int: int, long: int, long2: int) -> bool: ...
    def weakCompareAndSetRelease(self, int: int, long: int, long2: int) -> bool: ...
    def weakCompareAndSetVolatile(self, int: int, long: int, long2: int) -> bool: ...

_AtomicLongFieldUpdater__T = typing.TypeVar('_AtomicLongFieldUpdater__T')  # <T>
class AtomicLongFieldUpdater(typing.Generic[_AtomicLongFieldUpdater__T]):
    def accumulateAndGet(self, t: _AtomicLongFieldUpdater__T, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def addAndGet(self, t: _AtomicLongFieldUpdater__T, long: int) -> int: ...
    def compareAndSet(self, t: _AtomicLongFieldUpdater__T, long: int, long2: int) -> bool: ...
    def decrementAndGet(self, t: _AtomicLongFieldUpdater__T) -> int: ...
    def get(self, t: _AtomicLongFieldUpdater__T) -> int: ...
    def getAndAccumulate(self, t: _AtomicLongFieldUpdater__T, long: int, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable]) -> int: ...
    def getAndAdd(self, t: _AtomicLongFieldUpdater__T, long: int) -> int: ...
    def getAndDecrement(self, t: _AtomicLongFieldUpdater__T) -> int: ...
    def getAndIncrement(self, t: _AtomicLongFieldUpdater__T) -> int: ...
    def getAndSet(self, t: _AtomicLongFieldUpdater__T, long: int) -> int: ...
    def getAndUpdate(self, t: _AtomicLongFieldUpdater__T, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def incrementAndGet(self, t: _AtomicLongFieldUpdater__T) -> int: ...
    def lazySet(self, t: _AtomicLongFieldUpdater__T, long: int) -> None: ...
    _newUpdater__U = typing.TypeVar('_newUpdater__U')  # <U>
    @staticmethod
    def newUpdater(class_: typing.Type[_newUpdater__U], string: str) -> 'AtomicLongFieldUpdater'[_newUpdater__U]: ...
    def set(self, t: _AtomicLongFieldUpdater__T, long: int) -> None: ...
    def updateAndGet(self, t: _AtomicLongFieldUpdater__T, longUnaryOperator: typing.Union[java.util.function.LongUnaryOperator, typing.Callable]) -> int: ...
    def weakCompareAndSet(self, t: _AtomicLongFieldUpdater__T, long: int, long2: int) -> bool: ...

_AtomicMarkableReference__V = typing.TypeVar('_AtomicMarkableReference__V')  # <V>
class AtomicMarkableReference(typing.Generic[_AtomicMarkableReference__V]):
    def __init__(self, v: _AtomicMarkableReference__V, boolean: bool): ...
    def attemptMark(self, v: _AtomicMarkableReference__V, boolean: bool) -> bool: ...
    def compareAndSet(self, v: _AtomicMarkableReference__V, v2: _AtomicMarkableReference__V, boolean: bool, boolean2: bool) -> bool: ...
    def get(self, booleanArray: typing.List[bool]) -> _AtomicMarkableReference__V: ...
    def getReference(self) -> _AtomicMarkableReference__V: ...
    def isMarked(self) -> bool: ...
    def set(self, v: _AtomicMarkableReference__V, boolean: bool) -> None: ...
    def weakCompareAndSet(self, v: _AtomicMarkableReference__V, v2: _AtomicMarkableReference__V, boolean: bool, boolean2: bool) -> bool: ...

_AtomicReference__V = typing.TypeVar('_AtomicReference__V')  # <V>
class AtomicReference(java.io.Serializable, typing.Generic[_AtomicReference__V]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, v: _AtomicReference__V): ...
    def accumulateAndGet(self, v: _AtomicReference__V, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReference__V], typing.Callable]) -> _AtomicReference__V: ...
    def compareAndExchange(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> _AtomicReference__V: ...
    def compareAndExchangeAcquire(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> _AtomicReference__V: ...
    def compareAndExchangeRelease(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> _AtomicReference__V: ...
    def compareAndSet(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...
    def get(self) -> _AtomicReference__V: ...
    def getAcquire(self) -> _AtomicReference__V: ...
    def getAndAccumulate(self, v: _AtomicReference__V, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReference__V], typing.Callable]) -> _AtomicReference__V: ...
    def getAndSet(self, v: _AtomicReference__V) -> _AtomicReference__V: ...
    def getAndUpdate(self, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReference__V], typing.Callable]) -> _AtomicReference__V: ...
    def getOpaque(self) -> _AtomicReference__V: ...
    def getPlain(self) -> _AtomicReference__V: ...
    def lazySet(self, v: _AtomicReference__V) -> None: ...
    def set(self, v: _AtomicReference__V) -> None: ...
    def setOpaque(self, v: _AtomicReference__V) -> None: ...
    def setPlain(self, v: _AtomicReference__V) -> None: ...
    def setRelease(self, v: _AtomicReference__V) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReference__V], typing.Callable]) -> _AtomicReference__V: ...
    def weakCompareAndSet(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...
    def weakCompareAndSetAcquire(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...
    def weakCompareAndSetPlain(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...
    def weakCompareAndSetRelease(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...
    def weakCompareAndSetVolatile(self, v: _AtomicReference__V, v2: _AtomicReference__V) -> bool: ...

_AtomicReferenceArray__E = typing.TypeVar('_AtomicReferenceArray__E')  # <E>
class AtomicReferenceArray(java.io.Serializable, typing.Generic[_AtomicReferenceArray__E]):
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, eArray: typing.List[_AtomicReferenceArray__E]): ...
    def accumulateAndGet(self, int: int, e: _AtomicReferenceArray__E, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReferenceArray__E], typing.Callable]) -> _AtomicReferenceArray__E: ...
    def compareAndExchange(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> _AtomicReferenceArray__E: ...
    def compareAndExchangeAcquire(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> _AtomicReferenceArray__E: ...
    def compareAndExchangeRelease(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> _AtomicReferenceArray__E: ...
    def compareAndSet(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...
    def get(self, int: int) -> _AtomicReferenceArray__E: ...
    def getAcquire(self, int: int) -> _AtomicReferenceArray__E: ...
    def getAndAccumulate(self, int: int, e: _AtomicReferenceArray__E, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReferenceArray__E], typing.Callable]) -> _AtomicReferenceArray__E: ...
    def getAndSet(self, int: int, e: _AtomicReferenceArray__E) -> _AtomicReferenceArray__E: ...
    def getAndUpdate(self, int: int, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReferenceArray__E], typing.Callable]) -> _AtomicReferenceArray__E: ...
    def getOpaque(self, int: int) -> _AtomicReferenceArray__E: ...
    def getPlain(self, int: int) -> _AtomicReferenceArray__E: ...
    def lazySet(self, int: int, e: _AtomicReferenceArray__E) -> None: ...
    def length(self) -> int: ...
    def set(self, int: int, e: _AtomicReferenceArray__E) -> None: ...
    def setOpaque(self, int: int, e: _AtomicReferenceArray__E) -> None: ...
    def setPlain(self, int: int, e: _AtomicReferenceArray__E) -> None: ...
    def setRelease(self, int: int, e: _AtomicReferenceArray__E) -> None: ...
    def toString(self) -> str: ...
    def updateAndGet(self, int: int, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReferenceArray__E], typing.Callable]) -> _AtomicReferenceArray__E: ...
    def weakCompareAndSet(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...
    def weakCompareAndSetAcquire(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...
    def weakCompareAndSetPlain(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...
    def weakCompareAndSetRelease(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...
    def weakCompareAndSetVolatile(self, int: int, e: _AtomicReferenceArray__E, e2: _AtomicReferenceArray__E) -> bool: ...

_AtomicReferenceFieldUpdater__T = typing.TypeVar('_AtomicReferenceFieldUpdater__T')  # <T>
_AtomicReferenceFieldUpdater__V = typing.TypeVar('_AtomicReferenceFieldUpdater__V')  # <V>
class AtomicReferenceFieldUpdater(typing.Generic[_AtomicReferenceFieldUpdater__T, _AtomicReferenceFieldUpdater__V]):
    def accumulateAndGet(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReferenceFieldUpdater__V], typing.Callable]) -> _AtomicReferenceFieldUpdater__V: ...
    def compareAndSet(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V, v2: _AtomicReferenceFieldUpdater__V) -> bool: ...
    def get(self, t: _AtomicReferenceFieldUpdater__T) -> _AtomicReferenceFieldUpdater__V: ...
    def getAndAccumulate(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V, binaryOperator: typing.Union[java.util.function.BinaryOperator[_AtomicReferenceFieldUpdater__V], typing.Callable]) -> _AtomicReferenceFieldUpdater__V: ...
    def getAndSet(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V) -> _AtomicReferenceFieldUpdater__V: ...
    def getAndUpdate(self, t: _AtomicReferenceFieldUpdater__T, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReferenceFieldUpdater__V], typing.Callable]) -> _AtomicReferenceFieldUpdater__V: ...
    def lazySet(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V) -> None: ...
    _newUpdater__U = typing.TypeVar('_newUpdater__U')  # <U>
    _newUpdater__W = typing.TypeVar('_newUpdater__W')  # <W>
    @staticmethod
    def newUpdater(class_: typing.Type[_newUpdater__U], class2: typing.Type[_newUpdater__W], string: str) -> 'AtomicReferenceFieldUpdater'[_newUpdater__U, _newUpdater__W]: ...
    def set(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V) -> None: ...
    def updateAndGet(self, t: _AtomicReferenceFieldUpdater__T, unaryOperator: typing.Union[java.util.function.UnaryOperator[_AtomicReferenceFieldUpdater__V], typing.Callable]) -> _AtomicReferenceFieldUpdater__V: ...
    def weakCompareAndSet(self, t: _AtomicReferenceFieldUpdater__T, v: _AtomicReferenceFieldUpdater__V, v2: _AtomicReferenceFieldUpdater__V) -> bool: ...

_AtomicStampedReference__V = typing.TypeVar('_AtomicStampedReference__V')  # <V>
class AtomicStampedReference(typing.Generic[_AtomicStampedReference__V]):
    def __init__(self, v: _AtomicStampedReference__V, int: int): ...
    def attemptStamp(self, v: _AtomicStampedReference__V, int: int) -> bool: ...
    def compareAndSet(self, v: _AtomicStampedReference__V, v2: _AtomicStampedReference__V, int: int, int2: int) -> bool: ...
    def get(self, intArray: typing.List[int]) -> _AtomicStampedReference__V: ...
    def getReference(self) -> _AtomicStampedReference__V: ...
    def getStamp(self) -> int: ...
    def set(self, v: _AtomicStampedReference__V, int: int) -> None: ...
    def weakCompareAndSet(self, v: _AtomicStampedReference__V, v2: _AtomicStampedReference__V, int: int, int2: int) -> bool: ...

class DoubleAccumulator(java.util.concurrent.atomic.Striped64, java.io.Serializable):
    def __init__(self, doubleBinaryOperator: typing.Union[java.util.function.DoubleBinaryOperator, typing.Callable], double2: float): ...
    def accumulate(self, double: float) -> None: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def get(self) -> float: ...
    def getThenReset(self) -> float: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    def reset(self) -> None: ...
    def toString(self) -> str: ...

class DoubleAdder(java.util.concurrent.atomic.Striped64, java.io.Serializable):
    def __init__(self): ...
    def add(self, double: float) -> None: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    def reset(self) -> None: ...
    def sum(self) -> float: ...
    def sumThenReset(self) -> float: ...
    def toString(self) -> str: ...

class LongAccumulator(java.util.concurrent.atomic.Striped64, java.io.Serializable):
    def __init__(self, longBinaryOperator: typing.Union[java.util.function.LongBinaryOperator, typing.Callable], long2: int): ...
    def accumulate(self, long: int) -> None: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def get(self) -> int: ...
    def getThenReset(self) -> int: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    def reset(self) -> None: ...
    def toString(self) -> str: ...

class LongAdder(java.util.concurrent.atomic.Striped64, java.io.Serializable):
    def __init__(self): ...
    def add(self, long: int) -> None: ...
    def decrement(self) -> None: ...
    def doubleValue(self) -> float: ...
    def floatValue(self) -> float: ...
    def increment(self) -> None: ...
    def intValue(self) -> int: ...
    def longValue(self) -> int: ...
    def reset(self) -> None: ...
    def sum(self) -> int: ...
    def sumThenReset(self) -> int: ...
    def toString(self) -> str: ...

class Striped64: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.util.concurrent.atomic")``.

    AtomicBoolean: typing.Type[AtomicBoolean]
    AtomicInteger: typing.Type[AtomicInteger]
    AtomicIntegerArray: typing.Type[AtomicIntegerArray]
    AtomicIntegerFieldUpdater: typing.Type[AtomicIntegerFieldUpdater]
    AtomicLong: typing.Type[AtomicLong]
    AtomicLongArray: typing.Type[AtomicLongArray]
    AtomicLongFieldUpdater: typing.Type[AtomicLongFieldUpdater]
    AtomicMarkableReference: typing.Type[AtomicMarkableReference]
    AtomicReference: typing.Type[AtomicReference]
    AtomicReferenceArray: typing.Type[AtomicReferenceArray]
    AtomicReferenceFieldUpdater: typing.Type[AtomicReferenceFieldUpdater]
    AtomicStampedReference: typing.Type[AtomicStampedReference]
    DoubleAccumulator: typing.Type[DoubleAccumulator]
    DoubleAdder: typing.Type[DoubleAdder]
    LongAccumulator: typing.Type[LongAccumulator]
    LongAdder: typing.Type[LongAdder]
    Striped64: typing.Type[Striped64]
