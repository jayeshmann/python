def max_char(str):
    max_char = ''
    max_count = 0
    for i in str:
        count = str.count(i)
        if count > max_count:
            max_count = count
            max_char = i
    return max_char


print(max_char("ritika"))
