import re

page_info_rex = re.compile("(<.+>)|!|\s|\n|=")
undef_symbols_rex = re.compile("[\.\-\*]")


def get_full_text_merged():
    text = ""
    with open("voynich.txt", "r") as file:
        for line in file:
            line = page_info_rex.sub("", line)
            line = undef_symbols_rex.sub("", line)
            text += line

    return text


def get_full_text_normal():
    text = ""
    with open("C:/Users/kir/Desktop/voy/voynich.txt", "r") as file:
        for line in file:
            line = page_info_rex.sub("", line)
            text += line

    return text

