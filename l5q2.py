# Program to Print the Characters Which Are Common in Two Strings

a = 'abcdea'
b = 'xyzab'
a = set(a)

list = []

print("Common:")
for i in a:
    if(i in b):
        list.append(i)

print(*list)
