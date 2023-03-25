from os import system
import sys

cipher_freqs = {}   # ciphertext letter frequencies

ref_freqs = {   # reference letter frequencies. taken from the book, page 19
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0,
    'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7,
    'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8,
    'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1
}

key = { # used for constructing the key
    'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None,
    'H': None, 'I': None, 'J': None, 'K': None, 'L': None, 'M': None, 'N': None,
    'O': None, 'P': None, 'Q': None, 'R': None, 'S': None, 'T': None, 'U': None,
    'V': None, 'W': None, 'X': None, 'Y': None, 'Z': None
}

def frequency_analysis(filename: str):
    """Count ciphertext letter occurences and calculate relative percentages"""
    occurrences = {}
    file = open(filename, "r")
    while True:
        char = file.read(1)
        if not char:
            break
        if char in key.keys():
            if occurrences.get(char) is None:
                occurrences.update({char: 1})
            else:
                x = occurrences.get(char)
                occurrences.update({char: x + 1})
    file.close()
    chars = sum(occurrences.values())
    for letter, occurrence in occurrences.items():
        cipher_freqs.update({letter: round((occurrence / chars) * 100, 1)})

def input_loop(question: str, dict: dict) -> str:
    """Ask the user repeatedly for input"""
    while True:
        letter = input(question)
        if letter not in dict.keys():
            print("Wrong input, try again.")
            continue
        else:
            break
    return letter

def decrypt(filename: str) -> str:
    """Decrypt the ciphertext using the current key"""
    result = ""
    fin = open(filename, "r")
    while True:
        char = fin.read(1)
        if not char:
            break
        if char in cipher_freqs.keys() and key.get(char) is not None:
            result += key.get(char)
        else:
            result += char
    fin.close()
    return result

def main(argv: str):
    frequency_analysis(argv)
    while True:
        system('clear')
        print("Stage 1: Simple Monoalphabetic Substitution Cipher")
        print()
        print("Ciphertext letter frequencies:")
        print(dict(sorted(cipher_freqs.items(), key=lambda x:x[1], reverse=True)))
        print()
        print("Reference letter frequencies for English texts:")
        print(dict(sorted(ref_freqs.items(), key=lambda x:x[1], reverse=True)))
        print()
        print("Cipher alphabet: " + ' '.join(key.keys()))
        print("Plain alphabet:  ", end = '')
        for value in key.values():
            if value is not None:
                print(value + ' ', end = '')
            else:
                print('  ', end = '')
        print()
        print()
        plaintext = decrypt(argv)
        print(plaintext)
        if all(value is not None for value in key.values()):
            with open("plaintext.txt", 'w') as file: file.write(plaintext)
            print("Cryptanalysis complete! Plaintext saved to plaintext.txt")
            quit()
        else:
            cipher_letter = input_loop("Which ciphertext letter do you want to map? [A-Z]", key)
            plain_letter = input_loop("Which plaintext letter do you want to map it to? [a-z]", ref_freqs)
            key.update({cipher_letter: plain_letter})

if __name__ == "__main__":
    main(sys.argv[1])
