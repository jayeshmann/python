""" def checkPrime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
 """

n = int(input("Enter n > "))
l1 = []
count = 0
x = 2
while count != n:
    b = True
    for i in range(2, x):
        if x % i == 0:
            b = False
    if(b):
        count += 1
        l1.append(x)
    x += 1

print(l1)
