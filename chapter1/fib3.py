from typing import Dict
memo: Dict[int,int] = {0:0, 1:1}

def fib3(n:int) -> int:
    """
    much faster way than fib2
    :param n:
    :return: the n-th number of memo dictionary
    """

    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)

    return memo[n]

if __name__ == "__main__":
    print(fib3(50))
