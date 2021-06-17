def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a+b+c)


def strangeListFun(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList


# adding(4, c=2, b=3)
# adding(4, 2, b=3)

print(strangeListFun(5))
