import random

character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Multiplicative_encrypt(Plaintext, key):
    outText = []
    cryptText = []
    for eachLetter in Plaintext:
        if eachLetter in character:
            index = character.index(eachLetter)
            crypting = (index * key) % 26
            cryptText.append(crypting)
            newLetter = character[crypting]
            outText.append(newLetter)
    return outText


text = input('Type text to encrypt: ')
plaintext = str(text)
key = random.randint(0, 25)
print('Key:', key)
print('Ciphertext:', ''.join(Multiplicative_encrypt(plaintext, key)))
