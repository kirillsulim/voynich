__author__ = 'kir'

import os
from collections import Counter
import re

def letter_counts():
    cnt = Counter()
    for file in os.listdir("./clemtext"):
        if file.endswith(".lat"):
            with open(file) as so:
                for l in so:
                    for c in l:
                        c = c.lower()
                        if c not in "abcdefghijklmnopqrstuvwxyz":
                            continue
                        cnt[c] += 1
    #total = sum(cnt.values())
    #for it in sorted(cnt.items(), key=lambda it: it[1], reverse=True):
    #        print("{}: {:.2%}".format(it[0], it[1] / total ))
    return cnt



def get_words_counter():
    cnt = Counter()
    os.chdir("./clemtext")
    for file in os.listdir("."):
        if file.endswith(".lat"):
            with open(file) as so:
                for l in so:
                    words = re.split("\W+", l)
                    for w in words:
                        cnt[w.lower()] += 1
    del cnt[""]
    return cnt

#print(get_words_counter().most_common(10))
