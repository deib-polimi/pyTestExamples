#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:15:53 2020

@author: elisabettadinitto
"""

def pangram(text):
	for letter in [chr(ord('a')+i) for i in range(26)]:
		if letter not in text:
			return False
			break
	else:
		return True
    
    
def listPalindromes(text):
	found = []
	words = text.split()
	for word in words:
		if word == word[::-1]:
			found.append(word)
	return found

