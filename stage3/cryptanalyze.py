from collections import OrderedDict
from os import system
import numpy as np
import re
import string
import sys

ref_freqs = {   # reference letter frequencies. taken from the book, page 19
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0,
    'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7,
    'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8,
    'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1
}

def frequency_analysis_new(filename: str):
    occurrences = {}
    file = open(filename, "r")
    while True:
        char = file.read(1)
        if not char:
            break
        if occurrences.get(char) is None:
            occurrences.update({char: 1})
        else:
            x = occurrences.get(char)
            occurrences.update({char: x + 1})
    file.close()
    return dict(OrderedDict(sorted(occurrences.items(), key=lambda t: t[0])))

def frequency_percentages(occurrences):
    cipher_freqs = {}
    chars = sum(occurrences.values())
    for letter, occurrence in occurrences.items():
        cipher_freqs.update({letter: round((occurrence / chars) * 100, 1)})
    return cipher_freqs

def frequency_analysis(filename: str):
    """Count ciphertext letter occurences and calculate relative percentages"""
    occurrences = {}
    file = open(filename, "r")
    while True:
        char = file.read(1)
        if not char:
            break
        if char in list(string.ascii_uppercase) or char == '*':
            if occurrences.get(char) is None:
                occurrences.update({char: 1})
            else:
                x = occurrences.get(char)
                occurrences.update({char: x + 1})
    file.close()
    chars = sum(occurrences.values())
    for letter, occurrence in occurrences.items():
        cipher_freqs.update({letter: round((occurrence / chars) * 100, 1)})

def frequency_analysis_pairs(pairs):
    pair_freqs = {}
    for pair in pairs:
        if pair not in pair_freqs.keys():
            pair_freqs.update({pair: 1})
        else:
            x = pair_freqs.get(pair)
            pair_freqs.update({pair: x + 1})
    return pair_freqs

def split(filename: str):
    # split_text = ""
    # file = open(filename, "r")
    # count = 0
    # while True:
    #     char = file.read(1)
    #     if not char:
    #         break
    #     if char in list(string.ascii_uppercase) or char == '*':
    #         if count < 2:
    #             split_text += char
    #             count += 1
    #         else:
    #             split_text += " "
    #             split_text += char
    #             count = 1
    # file.close()
    # return split_text
    file = open(filename, "r")
    return re.findall('..', file.read())

def main(argv: str):
    print("Stage 3:")
    print()
    print("Ciphertext analysis")
    print()
    character_occurrences = frequency_analysis_new(argv)
    print("Amount of different characters: " + str(len(character_occurrences)))
    print()
    print("Ciphertext letter occurrences:")
    print(character_occurrences)
    print()
    print("Sorted occurrences:")
    print(dict(sorted(character_occurrences.items(), key=lambda x:x[1], reverse=True)))
    print()
    character_frequencies = frequency_percentages(character_occurrences)
    print("Ciphertext letter frequencies:")
    print(character_frequencies)
    print()
    print("Sorted ciphertext letter frequencies:")
    print(dict(sorted(character_frequencies.items(), key=lambda x:x[1], reverse=True)))
    #print(dict(sorted(cipher_freqs.items(), key=lambda x:x[1], reverse=True)))
    print()
    print("Reference letter frequencies for English texts:")
    print(dict(sorted(ref_freqs.items(), key=lambda x:x[1], reverse=True)))
    print()
    ciphertext_split = split(argv)
    print(ciphertext_split)
    print(len(ciphertext_split))
    #ciphertext_split.sort()
    #print(ciphertext_split)
    print()
    print(frequency_analysis_pairs(ciphertext_split))
    print(len(frequency_analysis_pairs(ciphertext_split)))
    print(dict(sorted(frequency_analysis_pairs(ciphertext_split).items(), key=lambda x:x[1], reverse=True)))

if __name__ == "__main__":
    main(sys.argv[1])