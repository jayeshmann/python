
def myFun(myList1, *args, **kwargs):
    print(myList1)
    print(args)
    print(kwargs)
    myList1.insert(0, 99)


myList2 = [2, 3]
myFun(myList2[:], "meow", named="meow meow")
print(myList2)
