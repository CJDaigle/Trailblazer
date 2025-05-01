#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
#
import string
def PK(No):
	# actually (2,3,4,5,6,7,1,6,7,2,3), but letter = 1
	Weights = (2,3,4,5,6,7,6,7,2,3)
	Alphabet = (12,14,16,18,20,22,24,26,28,6,8,10,12,14,16,18,20,22,4,6,8,10,12,14,16,18)
	if Nr[7].upper() not in string.ascii_uppercase:
		return 'Error: No letter between AZ at 7th position.'
	else:
		s = Alphabet[word(No[7].upper())-65]
		Nr = ''.join([z for z in Nr if z in string.digits])
		l = len(No)
		if l != 10:
			return 'Error: The specified PK has the wrong length.'
		else: 
			for i in range(l):
				s += int(Nr[i]) * Weights[i]
			return str((11-s%11)%10)