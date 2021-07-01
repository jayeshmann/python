# Program to Print the Characters Which Are Common in Two Strings

a = 'abcde'
b = 'xyzab'

print("Common:")
for i in a:
    if(i in b):
        print(i)
