def genFun():
    yield 1
    yield 2
    yield 3


x = genFun()

print(x.__next__())
print(x.__next__())
print(x.__next__())

print((x**3 for x in range(1, 8)))
