from os import _exit, fork
from time import sleep


class retry_n_times:
    def __init__(self, ntimes=3, timeout=3):
        self.ntimes = ntimes
        self.timeout = timeout

    def __call__(self, func):
        def _retry_n_times(*args, **kwargs):
            attempts = 0
            while attempts < self.ntimes:
                try:
                    ret = func(*args, **kwargs)
                except Exception:
                    sleep(self.timeout)
                else:
                    return ret
                attempts += 1

        return _retry_n_times


def memoize(func, cache={}):
    def _memoize(*args, **kwargs):
        # create an hashable key for the cache dict
        key = (args, str(kwargs))
        # check if result already in cache or add it
        if not key in cache:
            cache[key] = func(*args, **kwargs)
        else:
            print("Cache hit for key = %s" % str(key))

        return cache[key]

    return _memoize

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

@memoize
def fib_memoized(n):
    if n <= 1:
        return 1
    return fib_memoized(n-1) + fib_memoized(n-2)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib_memoized(100))


# two standard way to define a decorator
def decorator(func):
    def _decorator(*args, **kwargs):
        # something before the function is run
        ret = func(*args, **kwargs)
        # something after the function is run
        return ret

    return _decorator

@decorator
def to_decorate():
    print("Hello world")


to_decorate = decorator(to_decorate)

def param_deco(func):
    def _param_deco(arg1, arg2):
         def __param_deco(*args, **kwargs):
             pass

         return __param_deco
    return _param_deco


class call_decorator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def _decorator(*args, **kwargs):
            ret = func(*args, **kwargs)
            return ret

        return _decorator


def class_decorator(cls):
    def new_meth(self):
        return 100

    cls.new_meth = new_meth
    return cls


@class_decorator
class C1:
    pass

c = C1()
print(c.new_meth())


def on_forked_process(func):
    def _on_forked_process(*args, **kwargs):
        pid = fork()
        if pid == 0:
            # run the decorated function
            # in the child process
            func(*args, **kwargs)
            _exit(0)
        else:
            return pid

    return _on_forked_process


def naive_decorator(func, *args, **kwargs):
    # pre actions

    func(*args, **kwargs)

    # post actions


def verbose(original_function):
    def new_function(*args, **kwargs):
        print("Entering function %s" % original_function.__name__)
        ret = original_function(*args, **kwargs)
        print("Exiting function %s" % original_function.__name__)
        return ret

    return new_function
