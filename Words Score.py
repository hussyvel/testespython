# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:14:26 2019

@author: Hussyvel in Test
Words Score 
Possible Solution below
"""
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    return sum(sum(char in 'aeiouy' for char in word) % 2 or 2 for word in words)

n = int(input())
words = input().split()
print(score_words(words))
