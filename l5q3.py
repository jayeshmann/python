def checkString(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [
        chr(x) for x in range(97, 122) if chr(x) not in vowels]
    v, c, b, o = 0, 0, 0, 0
    for aChar in str1:
        if aChar in vowels:
            v += 1
        elif aChar in consonants:
            c += 1
        elif aChar == ' ':
            b += 1
        else:
            o += 1

    print(f"Vowels: {v}\nConsonants: {c}\nBlanks: {b}\nOthers: {o}")


if __name__ == '__main__':
    checkString(input("Enter a string=> "))
