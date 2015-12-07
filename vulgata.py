__author__ = 'kir'

import os
from collections import Counter

def print_letter_counts():
    cnt = Counter()
    os.chdir("./clemtext")
    for file in os.listdir("."):
        if file.endswith(".lat"):
            with open(file) as so:
                for l in so:
                    for c in l:
                        c = c.lower()
                        if c not in "abcdefghijklmnopqrstuvwxyz":
                            continue
                        cnt[c] += 1


    total = sum(cnt.values())

    for it in sorted(cnt.items(), key=lambda it: it[1], reverse=True):
        print("{}: {:.2%}".format(it[0], it[1] / total ))
