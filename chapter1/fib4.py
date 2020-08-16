from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n:int) -> int:
    """
    this decorator @lru_cache does caches all return values every time fib4() is called with new n value
    :param n:
    :return:
    """

    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)

if __name__ == "__main__":
    print(fib4(50))
