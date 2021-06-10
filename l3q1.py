l = [9, 5, 3, 2, 6, 8, 7, 1, 0, 4]

to_find = int(input("search for> "))
report = 'Failure'

for i in l:
    if to_find == i:
        report = 'Success'

print(report)
