from random import randint


def f():
    n = randint(0, 1000)
    l = 0
    for i in range(n):
        l += i
    return l


print(f())
