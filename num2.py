#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

import string

def PK(No):
    # Weights corresponding to the digits
    Weights = (2, 3, 4, 5, 6, 7, 6, 7, 2, 3)
    
    # Alphabet mapping (adjusted for clarity)
    Alphabet = {
        'A': 12, 'B': 14, 'C': 16, 'D': 18, 'E': 20, 'F': 22, 'G': 24, 'H': 26,
        'I': 28, 'J': 6, 'K': 8, 'L': 10, 'M': 12, 'N': 14, 'O': 16, 'P': 18,
        'Q': 20, 'R': 22, 'S': 4, 'T': 6, 'U': 8, 'V': 10, 'W': 12, 'X': 14,
        'Y': 16, 'Z': 18
    }
    
    # Check if the 7th character is a valid letter
    if No[6].upper() not in string.ascii_uppercase:
        return 'Error: No letter between A-Z at 7th position.'
    
    # Calculate initial value based on the 7th letter
    s = Alphabet.get(No[6].upper(), 0)
    
    # Remove non-digit characters and validate length
    No_digits = ''.join([z for z in No if z in string.digits])
    
    if len(No_digits) != 10:
        return 'Error: The specified PK has the wrong length.'
    
    # Calculate weighted sum
    for i in range(len(No_digits)):
        s += int(No_digits[i]) * Weights[i]
    
    # Calculate and return the check digit
    return str((11 - s % 11) % 10)
