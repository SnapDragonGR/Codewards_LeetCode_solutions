"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries
the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string, except for Haskell);
you need to return the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""

# Solution:


def DNA_strand(dna):
    comp_strand = []
    for letter in dna:
        if letter == "A":
            letter = "T"
            comp_strand.append(letter)
        elif letter == "T":
            letter = "A"
            comp_strand.append(letter)
        elif letter == "G":
            letter = "C"
            comp_strand.append(letter)
        elif letter == "C":
            letter = "G"
            comp_strand.append(letter)
    comp_strand_string = "".join(comp_strand)
    return comp_strand_string
