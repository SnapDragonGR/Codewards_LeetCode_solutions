"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

# Solution:

def get_count(sentence):
    vowel = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in sentence:
        if char in vowels:
            vowel += 1
    return vowel
