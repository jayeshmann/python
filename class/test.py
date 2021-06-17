
def myFun():
    global var
    var = False
    print("IsVisible?", var)


var = True
myFun()
print(var)
