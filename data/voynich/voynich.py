import re
from collections import Counter

page_info_rex = re.compile("(<.+>)|!|\s|\n|=")
undef_symbols_rex = re.compile("[\.\-]")

VOYNICH_FILE = "./data/voynich/voynich.txt"

class Cache:
    text_merged = ""
    text_full = ""
    first_page = ""

cache = Cache
cache.text_merged = ""
cache.text_full = ""

def get_full_text_merged():
    if not cache.text_merged:
        text = ""
        with open(VOYNICH_FILE, "r") as file:
            for line in file:
                line = page_info_rex.sub("", line)
                line = undef_symbols_rex.sub("", line)
                text += line

        cache.text_merged = text

    return cache.text_merged



def get_full_text_normal():
    if not cache.text_full:
        text = ""
        with open(VOYNICH_FILE, "r") as file:
            for line in file:
                line = page_info_rex.sub("", line)
                text += line

        text = text.replace("-\n", "")

    cache.text_full = text

    return cache.text_full

def get_first_page_normal():
    if not cache.first_page:
        text = ""
        with open(VOYNICH_FILE, "r") as file:
            for line in file:
                if not line.startswith("<f1r"):
                    continue

                line = page_info_rex.sub("", line)
                text += line

        text = text.replace("-", "")
        cache.first_page = text

    return cache.first_page


def get_alphabet():
    if not cache.text_merged:
        get_full_text_merged()

    counter = Counter(cache.text_merged)
    result = ""
    for letter, count in counter.most_common():
        result += letter

    return result



