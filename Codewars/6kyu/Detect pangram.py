"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

# Solution:

import string

def is_pangram(st):
    st = st.strip().lower().replace(' ', '')
    clean_st = ''
    for char in st:
        if char in string.ascii_letters:
            clean_st += char
    clean_st = set(clean_st)
    return sorted(string.ascii_lowercase) == sorted(clean_st)
