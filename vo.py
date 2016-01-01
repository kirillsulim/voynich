import re
from collections import Counter

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

