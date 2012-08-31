# simple memoize cache
def memoize(f, cache={}, *args, **kwargs):
    def _memoize(*args, **kwargs):
        key = (args, str(kwargs))
        if not key in cache:
            cache[key] = f(*args, **kwargs)

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


print(fib_memoized(100))
