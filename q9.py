c0 = int(input("Enter the nonZero and non-negative number"))
count = 0
arr = []

while(c0 != 1):
    if(c0 % 2 == 0):
        c0 = c0/2
        count += 1
        arr.append(c0)
    else:
        c0 = 3*c0+1
        count += 1
        arr.append(c0)


print([int(x) for x in arr])
print("steps =", count)
