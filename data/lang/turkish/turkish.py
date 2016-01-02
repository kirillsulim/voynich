

ALPHABET = "abcçdefgğhıijklmnoöprsştuüvyz"
WORDS_FILE = "./data/lang/turkish/words.txt"


class Cache:
    words = None

cache = Cache()


def get_alphabet():
    return ALPHABET

def get_words():
    if not cache.words:
        words = []
        with open(WORDS_FILE, "r") as file:
            for line in file:
                words.append(line.strip(" \r\n\t"))
        cache.words = words

    return cache.words
