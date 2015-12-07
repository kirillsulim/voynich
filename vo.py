import re
from collections import Counter
import string
import textwrap

page_info_rex = re.compile("(<.+>)|!|\s|\n|=")
undef_symbols_rex = re.compile("[\.\-\*]")

shade_words = [
    #"ok",
    #"ol",
    #"aiin",
    #"che",
    #"eedy",
    #"dain",
    #"sh",
    #"ii",
    #"iii",
    #"sh",
    #"ee",
    #"ch",
    #"edy"
    "aiin",
    "ain",
    "sh",
    "iiin",
]

# http://www.sttmedia.com/characterfrequency-latin
latin_langtable = "IEAUTSRNOMCLPDBQGVFHXYZ".lower()
latin_vulgata_table = "eitusanrmocdlpbvqgfhjxyzk"
italian_langtable = "EAIONTRLSCDUPMVGHBFZQ".lower()
spanish_langtable = "EAOSNRILDTUCMPBHQYVGÓÍFJZÁÉÑXÚKWÜ".lower()


shade_words_rex = re.compile("|".join(shade_words))


words_counter = Counter()

text_onliner = ""
clean_onliner = ""

all_words = []

with open("voynich.txt", "r") as file:
    for line in file:
        if not line.startswith("<f1r"):
            continue
        line = page_info_rex.sub("", line)

        text_onliner += line

        line = shade_words_rex.sub("", line)

        clean_onliner += line



        words = undef_symbols_rex.split(line)
        all_words.extend(words)
        for w in words:
            words_counter[w] += 1

print(words_counter.most_common(10))


def count_someftongs(length, list):
    counter = Counter()
    for word in list:
        for i in range(0, len(word) - length +1):
            counter[word[i:i+length]] += 1
    return counter

def sort_keys(counter):
    return sorted(counter.items(), key=lambda tpl: tpl[1], reverse=True)

def good_print(ag):
    counter = Counter(ag)
    total = sum(counter.values())
    smftong_count = len(counter.items())
    print("Smftong total: ", smftong_count)
    for item in sort_keys(counter):
        print("{}: {:.2%}".format(item[0], item[1] / total))


def create_trans_table(ag, langtable):
    counter = Counter(ag)
    lang = str(langtable)
    voo = ""
    for item in sort_keys(counter):
        voo += item[0]

    if len(voo) > len(lang):
        lang += "@#$%^&*"
    lang = lang[:len(voo)]

    print("Table created:")
    print(voo, len(voo))
    print(lang, len(lang))

    return {voo[i]: lang[i] for i in range(len(voo))}



######################################
let_counter = count_someftongs(1, all_words)
let2_counter = count_someftongs(2, all_words)
let3_counter = count_someftongs(3, all_words)
let4_counter = count_someftongs(4, all_words)


good_print(let_counter)

def mytrans(string, dict):
    def conv(char):
        if char == ".":
            return char
        if char == "-":
            return char
        if char in dict:
            return dict[char]
        else:
            return "?"


    return "".join([conv(c) for c in string])

def create_manual_table(frm, tw):
    if len(frm) > len(tw):
        tw += "@#$%^&*"
    tw = tw[:len(frm)]

    print("Table created:")
    print(frm, len(frm))
    print(tw, len(tw))

    return {frm[i]: tw[i] for i in range(len(frm))}

mantable = create_manual_table(
    "yohedacrstqlkinpmf%gxvz",
    "eitusanrmocglpbvqdfhjxy",
    #^^^^^^^^^^
)

for it in let2_counter.most_common(10):
    print(it[0], mytrans(it[0], mantable))

for it in let3_counter.most_common(10):
    print(it[0], mytrans(it[0], mantable))

for it in let4_counter.most_common(10):
    print(it[0], mytrans(it[0], mantable))




#print(text_onliner[:200])
#print("latin:", textwrap.fill(mytrans(clean_onliner[:1000], create_trans_table(let_counter, latin_vulgata_table)), 150))
print("latin:", textwrap.fill(mytrans(clean_onliner[:5000], mantable), 150))
#print("italian:", mytrans(trnsalatble, create_trans_table(let_counter, italian_langtable)))
#print("spania:", mytrans(trnsalatble, create_trans_table(let_counter, spanish_langtable)))

print("\n\n")
print("orig:", textwrap.fill(text_onliner[:5000], 150))

