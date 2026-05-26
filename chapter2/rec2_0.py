import re
from collections import Counter

#!/usr/bin/env python3
# File: /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter2/rec2_0.py
# Illustrate string manipulation:
# 1) Reverse a word
# 2) Find vowels in a fixed sentence
# 3) Find palindromes in a sentence (preferably 10 words)


VOWELS = set("aeiouAEIOU")


def reverse_word(word: str) -> str:
    """Return the reversed word."""
    return word[::-1]


def vowels_in_sentence(sentence: str) -> Counter:
    """Return a Counter of vowels found in the sentence (case-insensitive)."""
    vowels = [ch.lower() for ch in sentence if ch in VOWELS]
    return Counter(vowels)


def clean_word(word: str) -> str:
    """Remove non-alphanumeric characters and lowercase."""
    return re.sub(r'[^A-Za-z0-9]', '', word).lower()


def find_palindromes(sentence: str, min_length: int = 2) -> list:
    """Return list of palindromic words from the sentence (ignores punctuation/case)."""
    words = sentence.split()
    palindromes = []
    for w in words:
        cw = clean_word(w)
        if len(cw) >= min_length and cw == cw[::-1]:
            palindromes.append(w)  # return original word form
    return palindromes


def main():
    # Task 1: Reverse a word (prompt user)
    word = input("Enter a word to reverse: ").strip()
    if word:
        print("Reversed:", reverse_word(word))
    else:
        print("No word entered; skipping reverse demo.")

    # Task 2: Find vowels in the given sentence
    sentence2 = "Jack and Jill went up the hill"
    print("\nSentence for vowel scan:\n", sentence2)
    vowel_counts = vowels_in_sentence(sentence2)
    all_vowels_sequence = "".join([ch for ch in sentence2 if ch in VOWELS])
    print("Vowels found (in order):", all_vowels_sequence)
    print("Vowel counts:", dict(vowel_counts))

    # Task 3: Find palindromes in a sentence (expecting ~10 words)
    print("\nTask 3: Enter a sentence (10 words recommended). Press Enter to use a default 10-word example.")
    user_sentence = input("Sentence: ").strip()
    default_example = "level radar civic rotor kayak refer madam noon stats deed"  # 10 words, many palindromes
    if not user_sentence:
        sentence3 = default_example
        print("Using default sentence:\n", sentence3)
    else:
        sentence3 = user_sentence
        count_words = len(sentence3.split())
        if count_words != 10:
            print(f"Note: provided sentence has {count_words} words (not 10). Processing anyway.")

    pal = find_palindromes(sentence3)
    if pal:
        print("Palindromic words found:", pal)
    else:
        print("No palindromic words found.")


if __name__ == "__main__":
    main()