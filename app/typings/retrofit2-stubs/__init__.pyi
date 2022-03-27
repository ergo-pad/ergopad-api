import java.lang
import java.lang.annotation
import java.lang.reflect
import java.net
import java.util
import java.util.concurrent
import okhttp3
import retrofit2.converter
import retrofit2.http
import retrofit2.internal
import typing



_Call__T = typing.TypeVar('_Call__T')  # <T>
class Call(java.lang.Cloneable, typing.Generic[_Call__T]):
    def cancel(self) -> None: ...
    def clone(self) -> 'Call'[_Call__T]: ...
    def enqueue(self, callback: 'Callback'[_Call__T]) -> None: ...
    def execute(self) -> 'Response'[_Call__T]: ...
    def isCanceled(self) -> bool: ...
    def isExecuted(self) -> bool: ...
    def request(self) -> okhttp3.Request: ...

_CallAdapter__R = typing.TypeVar('_CallAdapter__R')  # <R>
_CallAdapter__T = typing.TypeVar('_CallAdapter__T')  # <T>
class CallAdapter(typing.Generic[_CallAdapter__R, _CallAdapter__T]):
    def adapt(self, call: Call[_CallAdapter__R]) -> _CallAdapter__T: ...
    def responseType(self) -> java.lang.reflect.Type: ...
    class Factory:
        def __init__(self): ...
        def get(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], retrofit: 'Retrofit') -> 'CallAdapter'[typing.Any, typing.Any]: ...

_Callback__T = typing.TypeVar('_Callback__T')  # <T>
class Callback(typing.Generic[_Callback__T]):
    def onFailure(self, call: Call[_Callback__T], throwable: java.lang.Throwable) -> None: ...
    def onResponse(self, call: Call[_Callback__T], response: 'Response'[_Callback__T]) -> None: ...

_Converter__F = typing.TypeVar('_Converter__F')  # <F>
_Converter__T = typing.TypeVar('_Converter__T')  # <T>
class Converter(typing.Generic[_Converter__F, _Converter__T]):
    def convert(self, f: _Converter__F) -> _Converter__T: ...
    class Factory:
        def __init__(self): ...
        def requestBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], annotationArray2: typing.List[java.lang.annotation.Annotation], retrofit: 'Retrofit') -> 'Converter'[typing.Any, okhttp3.RequestBody]: ...
        def responseBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], retrofit: 'Retrofit') -> 'Converter'[okhttp3.ResponseBody, typing.Any]: ...
        def stringConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], retrofit: 'Retrofit') -> 'Converter'[typing.Any, str]: ...

class HttpException(java.lang.RuntimeException):
    def __init__(self, response: 'Response'[typing.Any]): ...
    def code(self) -> int: ...
    def message(self) -> str: ...
    def response(self) -> 'Response'[typing.Any]: ...

class Invocation:
    def arguments(self) -> java.util.List[typing.Any]: ...
    def method(self) -> java.lang.reflect.Method: ...
    @staticmethod
    def of(method: java.lang.reflect.Method, list: java.util.List[typing.Any]) -> 'Invocation': ...
    def toString(self) -> str: ...

_Response__T = typing.TypeVar('_Response__T')  # <T>
class Response(typing.Generic[_Response__T]):
    def body(self) -> _Response__T: ...
    def code(self) -> int: ...
    _error_0__T = typing.TypeVar('_error_0__T')  # <T>
    _error_1__T = typing.TypeVar('_error_1__T')  # <T>
    @typing.overload
    @staticmethod
    def error(int: int, responseBody: okhttp3.ResponseBody) -> 'Response'[_error_0__T]: ...
    @typing.overload
    @staticmethod
    def error(responseBody: okhttp3.ResponseBody, response2: okhttp3.Response) -> 'Response'[_error_1__T]: ...
    def errorBody(self) -> okhttp3.ResponseBody: ...
    def headers(self) -> okhttp3.Headers: ...
    def isSuccessful(self) -> bool: ...
    def message(self) -> str: ...
    def raw(self) -> okhttp3.Response: ...
    _success_0__T = typing.TypeVar('_success_0__T')  # <T>
    _success_1__T = typing.TypeVar('_success_1__T')  # <T>
    _success_2__T = typing.TypeVar('_success_2__T')  # <T>
    _success_3__T = typing.TypeVar('_success_3__T')  # <T>
    @typing.overload
    @staticmethod
    def success(int: int, t: _success_0__T) -> 'Response'[_success_0__T]: ...
    @typing.overload
    @staticmethod
    def success(t: _success_1__T) -> 'Response'[_success_1__T]: ...
    @typing.overload
    @staticmethod
    def success(t: _success_2__T, headers: okhttp3.Headers) -> 'Response'[_success_2__T]: ...
    @typing.overload
    @staticmethod
    def success(t: _success_3__T, response: okhttp3.Response) -> 'Response'[_success_3__T]: ...
    def toString(self) -> str: ...

class Retrofit:
    def baseUrl(self) -> okhttp3.HttpUrl: ...
    def callAdapter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation]) -> CallAdapter[typing.Any, typing.Any]: ...
    def callAdapterFactories(self) -> java.util.List[CallAdapter.Factory]: ...
    def callFactory(self) -> okhttp3.Call.Factory: ...
    def callbackExecutor(self) -> java.util.concurrent.Executor: ...
    def converterFactories(self) -> java.util.List[Converter.Factory]: ...
    _create__T = typing.TypeVar('_create__T')  # <T>
    def create(self, class_: typing.Type[_create__T]) -> _create__T: ...
    def newBuilder(self) -> 'Retrofit.Builder': ...
    def nextCallAdapter(self, factory: CallAdapter.Factory, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation]) -> CallAdapter[typing.Any, typing.Any]: ...
    _nextRequestBodyConverter__T = typing.TypeVar('_nextRequestBodyConverter__T')  # <T>
    def nextRequestBodyConverter(self, factory: Converter.Factory, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], annotationArray2: typing.List[java.lang.annotation.Annotation]) -> Converter[_nextRequestBodyConverter__T, okhttp3.RequestBody]: ...
    _nextResponseBodyConverter__T = typing.TypeVar('_nextResponseBodyConverter__T')  # <T>
    def nextResponseBodyConverter(self, factory: Converter.Factory, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation]) -> Converter[okhttp3.ResponseBody, _nextResponseBodyConverter__T]: ...
    _requestBodyConverter__T = typing.TypeVar('_requestBodyConverter__T')  # <T>
    def requestBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], annotationArray2: typing.List[java.lang.annotation.Annotation]) -> Converter[_requestBodyConverter__T, okhttp3.RequestBody]: ...
    _responseBodyConverter__T = typing.TypeVar('_responseBodyConverter__T')  # <T>
    def responseBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation]) -> Converter[okhttp3.ResponseBody, _responseBodyConverter__T]: ...
    _stringConverter__T = typing.TypeVar('_stringConverter__T')  # <T>
    def stringConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation]) -> Converter[_stringConverter__T, str]: ...
    class Builder:
        def __init__(self): ...
        def addCallAdapterFactory(self, factory: CallAdapter.Factory) -> 'Retrofit.Builder': ...
        def addConverterFactory(self, factory: Converter.Factory) -> 'Retrofit.Builder': ...
        @typing.overload
        def baseUrl(self, string: str) -> 'Retrofit.Builder': ...
        @typing.overload
        def baseUrl(self, uRL: java.net.URL) -> 'Retrofit.Builder': ...
        @typing.overload
        def baseUrl(self, httpUrl: okhttp3.HttpUrl) -> 'Retrofit.Builder': ...
        def build(self) -> 'Retrofit': ...
        def callAdapterFactories(self) -> java.util.List[CallAdapter.Factory]: ...
        def callFactory(self, factory: okhttp3.Call.Factory) -> 'Retrofit.Builder': ...
        def callbackExecutor(self, executor: java.util.concurrent.Executor) -> 'Retrofit.Builder': ...
        def client(self, okHttpClient: okhttp3.OkHttpClient) -> 'Retrofit.Builder': ...
        def converterFactories(self) -> java.util.List[Converter.Factory]: ...
        def validateEagerly(self, boolean: bool) -> 'Retrofit.Builder': ...

class RetrofitUtil:
    def __init__(self): ...
    _invokeServiceMethod__T = typing.TypeVar('_invokeServiceMethod__T')  # <T>
    @staticmethod
    def invokeServiceMethod(retrofit: Retrofit, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> Call[_invokeServiceMethod__T]: ...

class SkipCallbackExecutor(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("retrofit2")``.

    Call: typing.Type[Call]
    CallAdapter: typing.Type[CallAdapter]
    Callback: typing.Type[Callback]
    Converter: typing.Type[Converter]
    HttpException: typing.Type[HttpException]
    Invocation: typing.Type[Invocation]
    Response: typing.Type[Response]
    Retrofit: typing.Type[Retrofit]
    RetrofitUtil: typing.Type[RetrofitUtil]
    SkipCallbackExecutor: typing.Type[SkipCallbackExecutor]
    converter: retrofit2.converter.__module_protocol__
    http: retrofit2.http.__module_protocol__
    internal: retrofit2.internal.__module_protocol__