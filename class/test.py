from itertools import chain

test_list = ["meow", ' ', 'm', 'e', 'o', 'w']

print(test_list)

res = list(chain.from_iterable(test_list))

print(res)
