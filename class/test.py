def genFun():
    yield 1
    yield 2
    yield 3


x = genFun()

print(x.__next__())
print(x.__next__())
print(x.__next__())
