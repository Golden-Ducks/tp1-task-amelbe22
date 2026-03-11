# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:09:09 2026

@author: HP
"""

import re
from num2words import num2words


def clean_text(text):
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', ' ', text)
    
    text = re.sub(r'\d+', ' ', text)
    
    symbols = ['@', '#', '$', '%', '&', '*']
    for sym in symbols:
        text = text.replace(sym, ' ')
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


with open("task1.txt", "r") as f:
    sample_text = f.read()

cleaned = clean_text(sample_text)
print(cleaned)
"""You can smartly distinguish between meaningful % 
and noise by using a regular expression that keeps % 
only when it directly follows a digit (like in 88%) 
and removes it in all other contexts (such as %% or 1%st) 
using lookahead and lookbehind conditions."""


with open("task2.txt", "r") as f:
    text = f.read() 


def normalize_text(text):
    text = text.lower()
    
    text = re.sub(r'\d+', lambda x: num2words(int(x.group())), text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


print(normalize_text(text))







