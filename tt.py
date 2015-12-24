

import voynich
import vulgata
from gen.populate import GenMaster, string_mutator
from gen.comparation import compare
from vo import mytrans, create_manual_table
import textwrap

part = voynich.get_full_text_merged()[:1000]

alphabet = "eitusanrmocdlpbvqgfhjxy"
voalphabet = "yohedacrstqlkinpmf%gxvz"

popu = []
for i in range(100):
    popu.append(string_mutator(alphabet, 2))

master = GenMaster(popu)

vulgata_words = vulgata.get_words_counter().most_common(100)

def transl(alphabet):
    decrypted = mytrans(part, create_manual_table(voalphabet, alphabet))
    #print("[decripted]: ", decrypted)
    resu = 0.
    for w in list(map(lambda it: it[0], vulgata_words)):
        resu += compare(decrypted, w)
    return resu


data = "sciens hoc quia lex justo non est posita, sed injustis, et non subditis, impiis, et peccatoribus, sceleratis, et contaminatis, parricidis, et matricidis, homicidis"

enc = mytrans(
    data,
    create_manual_table(
        alphabet,
        voalphabet
    )
)

def trans_enc(alphabet):
    decrypted = mytrans(part, create_manual_table(voalphabet, alphabet))
    print("[decripted]: ", decrypted)
    resu = 0.
    for w in list(map(lambda it: it[0], vulgata_words)):
        resu += compare(decrypted, w)
    return resu

for i in range(0):
    master.generation(transl)



zzz = voynich.get_full_text_normal()[:1500]

trrrr = mytrans(
    zzz,
    create_manual_table(
        voalphabet,
        "aeinrlkdmyutsnouszgchgvcopfj"
    )
)

print(textwrap.fill(trrrr, 150))




