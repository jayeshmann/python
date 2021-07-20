"""
input
wjmzbmr

output
CHAT WITH HER!

input
xiaodao

output
IGNORE HIM!

input
sevenkplus

output
CHAT WITH HER!
"""
# Find number of distinct characters is odd or even, if odd print "IGNORE HIM!" otherwise print "CHAT WITH HER!"


def chat_with_her(s):
    if len(set(s)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


name = input()
chat_with_her(name)
