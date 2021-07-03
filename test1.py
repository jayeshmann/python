def checkPrime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


n = int(input("Enter n > "))
l1 = []
x = 2
while len(l1) != n:
    if(checkPrime(x)):
        l1.append(x)
    x += 1

print(l1)
