#!/usr/local/bin/checkio --domain=py run pangram

# A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a    sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The    quick brown fox jumps over the lazy dog".
# 
# For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation    symbols. You need to check if the sentence is a pangram or not. Case does not matter.
# 
# Input:A text as a string.
# 
# Output:Whether the sentence is a pangram or not as a boolean.
# 
# Precondition:
# 
# all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
# 0 < len(text)
# END_DESC

def check_pangram(text):
    a_z =[chr(i) for i in range(97, 97+26)]
    for i in a_z:
        if i in text.lower():
            continue
        else:
            return False
    return True