c0 = int(input())
count = 0
list = []

while(c0 != 1):
    if(c0 % 2 == 0):
        c0 = c0//2
        count += 1
        list.append(c0)
    else:
        c0 = 3*c0+1
        count += 1
        list.append(c0)


print(*list, "steps =", count)
