import random
from difflib import SequenceMatcher
import datetime
import functools
import math
import logging as log


# get string, mutate it
def string_mutator(string, mut_coeff=0.3):
    if mut_coeff < 1:
        if random.randrange(math.ceil(1/mut_coeff)) != 0:
            return string
        else:
            mut_coeff = 1
    count = len(string)
    for i in range(math.floor(mut_coeff)):
        string = swap(string, random.randrange(count), random.randrange(count))
    return string


def swap(s, i, j):
    if i < j:
        return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))
    elif j < i:
        return ''.join((s[:j], s[i], s[j+1:i], s[j], s[i+1:]))
    else:
        return s


def string_sexuator(strings):
    random.shuffle(strings)
    result = []
    for i in range(len(strings)):
        s1 = strings[i]
        if i == 0:
            s2 = strings[-1]
        else:
            s2 = strings[i-1]
        result.append(copulate_strings(s1, s2))
    return result


def copulate_strings(s1, s2):
    child = str(s1)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if random.randrange(2) == 0:
                child = swap(child, i, child.index(s2[i]))
    return child


class GenMaster:
    def __init__(self, start_population):
        self.population = start_population

    def generation(self, function, maximize=True):
        log.info("Generation started")

        mp = {}
        for spec in self.population:
            value = function(spec);
            mp[spec] = value
            log.debug("Added %s with value %d", spec, value)

        log.debug("Population dictionary: %s", mp)
        log.info("Mean value for population: %d", sum(mp.values())/len(mp))
        self.population = sorted(mp, key=lambda x: x[1])

        # get children twice
        next_gen = list(map(lambda s: string_mutator(s), string_sexuator(self.population[:len(self.population)//2])))
        next_gen.extend(list(map(lambda s: string_mutator(s), string_sexuator(self.population[:len(self.population)//2]))))

        #next_gen = list(map(lambda s: string_mutator(s), self.population[:len(self.population)//2]))
        #next_gen.extend(list(map(lambda s: string_mutator(s), self.population[:len(self.population)//2])))

        self.population = next_gen


#master = GenMaster("abcdefghijk", 100)

def distance(string):
    cc = 0
    tester = "abcdefghijk"
    for i in range(len(string)):
        if string[i] == tester[i]:
            cc += 1
    return cc



#for i in range(100):
#    st = datetime.datetime.now()
#    print("Generation {}".format(i))
#    master.generation(distance)
#    print("Mean distance: ", sum([distance(x) for x in master.population]) / 100)
#    print("Best: ", sorted(master.population, key=lambda s: distance(s), reverse=True)[:10])
#    print(datetime.datetime.now() - st, len(master.population))

#print(master.population)

#for x in ['edgjchikafb', 'jgkiecdfahb', 'cbgjhideafk', 'cfgjhikbaed', 'jagihfdeckb', 'ajeigfdkchb', 'bgjcifkaehd', 'icefhbdajkg', 'dahjibgkcef', 'faihebgjckd', 'ehijbkfgcad', 'iagjbkfehdc', 'gachbfdjkie', 'kgbfcedjiha', 'jagbidekfch', 'agfkibhcdje', 'kgiahefcdjb', 'chfidjgaebk', 'hjkcefgadbi', 'ihgabfjdekc', 'ahjicgdefkb', 'jabfckdhige', 'jbcfkedhiga', 'cbjgdhaefik', 'cijfdhbagke', 'abdhgcijekf', 'ajghbdicefk', 'afgkhdijebc', 'kcafibgjedh', 'kagfjeihbdc', 'eafghdijcbk', 'jbfdhekgcia', 'dgifhceakbj', 'aiejhfdgcbk', 'ijagedfkcbh', 'cdhjiefgkba', 'cjfkbdaehgi', 'djekbhacigf', 'jdifbhacekg', 'ajehbfdickg', 'jaegcfkibhd', 'jbfacekighd', 'kgbicehfjad', 'jgbikfdecha', 'jgekfbdciah', 'jgekibfcdha', 'bkdecjgihfa', 'fkbgejcihda', 'fdihceabgkj', 'jbdhcegkaif', 'jfkihdgbcea', 'chfjbidakeg', 'dgbjhaickef', 'daghfbicjek', 'dcghbkaejif', 'gbkfejdhica', 'bkehfjgidca', 'fjihebadgkc', 'fciabhjkged', 'hicjfegkadb', 'kgafbcihjde', 'abfgceihjkd', 'cifgkeahdbj', 'gdjfihaecbk', 'edhkijfcgab', 'agihedfcjkb', 'abcjhkdigfe', 'ibfjhcegkda', 'jgiehcafkdb', 'jfbhigkcead', 'bgifajcdehk', 'fkajigcdehb', 'ajfibgcedhk', 'djekbhfacgi', 'bikjcdfghae', 'bageckdihfj', 'akbijhdefcg', 'bkfjehgaicd', 'bahkefgjicd', 'jbghcdekiaf', 'jbiacekdghf', 'jkagcbdfihe', 'cgekijdbfha', 'fbaiekjhcgd', 'egijfkdchba', 'cghjkiaefbd', 'ajbfkidechg', 'ajgfhdikebc', 'gjbahdicefk', 'jdbahcifekg', 'ahkfdjcebig', 'afbhiedjkgc', 'afgibkhjced', 'dieabkjfcgh', 'ajefchdigbk', 'jifhdkcbgae', 'jcfkidbghae', 'fackibgjhde', 'jaekhfgidbc', 'jaekhdgbcif']:
#    print(distance(x))






