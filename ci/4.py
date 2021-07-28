"""
efficient function to return maximum occurring character in the input string e.g., if input string is “test” then function should return ‘t’
"""


def max_char(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    max_char = ''
    max_count = 0
    for i in freq:
        if freq.get(i) > max_count:
            max_char = i
            max_count = freq.get(i)
    return max_char


print(max_char("ritika"))
