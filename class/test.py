l = ['Cat', 'says', 'meow']
print(l)

l.remove('says')
l[1] = 'meows'

print(l)


l = list(filter(lambda x: x if x == 'Cat' else '', l))
print(l)
