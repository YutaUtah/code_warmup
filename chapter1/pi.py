# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11

def calculate_pi(n):
    numerator = 4
    pi = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            pi -= numerator / ((i-1)*2 + 1)
        else:
            pi += numerator / ((i - 1) * 2 + 1)
    return pi


if __name__ == "__main__":
    pi = calculate_pi(100000)
    print(pi)
