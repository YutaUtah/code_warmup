def fib2(n: int) -> int:
    """

    :param n:
    :return: fibonacci number in a given index but its taking too much time
    """
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

if __name__ == "__main__":
    print(fib2(50))