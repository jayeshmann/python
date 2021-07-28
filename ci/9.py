"""
Find frequency of each word in a string'

"""


def word_freq(string):
    freq = {}
    for word in string.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


print(word_freq('The quick brown fox jumps over the lazy dog cat cat'))
