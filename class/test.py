str1 = ''
str2 = 'meow'

print(bool(str1) == False)
print(bool(str2) == True)

print(repr(str1 and str2))

print(repr(str2 and str1))

print(repr(str1 or str2))

print(repr(str2 or str1))
