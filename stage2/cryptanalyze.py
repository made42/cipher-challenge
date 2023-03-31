from os import system
import string
import sys

cipher_alphabet = list(string.ascii_uppercase)
plain_alphabet = list(string.ascii_lowercase)

def decrypt(ciphertext: str) -> str:
    plaintext = ""
    for char in ciphertext:
        if char in cipher_alphabet:
            index = cipher_alphabet.index(char)
            plaintext += plain_alphabet[index]
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    ciphertext = open(sys.argv[1], 'r').read()
    while True:
        system('clear')
        print("Stage 2: Caesar Shift Cipher")
        print()
        print("Ciphertext:" + ciphertext)
        print("Cipher alphabet: " + ' '.join(cipher_alphabet))
        print("Plain alphabet : " + ' '.join(plain_alphabet))
        print()
        print("Plaintext: " + decrypt(ciphertext))
        input("Press any key to shift...")
        plain_alphabet.append(plain_alphabet.pop(0))
