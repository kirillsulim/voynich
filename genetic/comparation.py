__author__ = 'kir'

from difflib import SequenceMatcher

def compare(text, part):
    count = 0.
    for i in range(len(text) - len(part)):
        count += distance(part, text[i:i+len(part)])
    return count

def distance(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()



