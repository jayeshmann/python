def checkString(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [
        x for x in 'b,c,d,f,g,h,i,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'.split(',')]
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
