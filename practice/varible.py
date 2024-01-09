def myfunc(n):
    return lambda a : a * n
doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))
print(tripler(11))