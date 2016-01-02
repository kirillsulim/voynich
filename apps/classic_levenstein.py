from fuzzywuzzy import fuzz

import logging as log

from genetic.populate import GenMaster, string_mutator
from langtools.translate import Translator
from langtools.text_distance import text_distance
import data.voynich.voynich as voy
import data.lang.turkish.turkish as turk


def run():
    vo_alphabet = voy.get_alphabet()
    turk_alphabet = turk.get_alphabet()

    vo_words = voy.get_first_page_normal().split(".")

    log.debug("Voynich words from 1st page: %s", vo_words)

    turk_words = turk.get_words()[:100]

    log.debug("Get %d turkish words", len(turk_words))

    def dist(s1, s2):
        return 100 - fuzz.ratio(s1, s2)

    def calculate(tralph):
        tr = Translator(vo_alphabet, tralph)
        words_translated = [tr.trans(w) for w in vo_words]

        return text_distance(words_translated, turk_words, dist)

    log.info("Generate population...")
    population = []
    for i in range(100):
        population.append(string_mutator(turk_alphabet, len(turk_alphabet)))

    log.info("Population generated")

    gm = GenMaster(population)

    for i in range(100):
        log.info("Start %d generation calculation", i)
        gm.generation(calculate)
        log.info("Calculation terminated")
        log.debug("%d generation is: %s", i, gm.population)

        tr = Translator(vo_alphabet, gm.population[0])
        translated = " ".join([tr.trans(w) for w in vo_words])
        log.info("Translated text: %s", translated)

    log.info("Final generation is: %s", gm.population)













