import re
from networkx import Graph, shortest_path_length, has_path

vowels = "aioue"
consonants = "qwrtpsdfghjklmnbvcxz"


re_vowels = re.compile("[" + vowels + "]")
re_consonants = re.compile("[" + consonants + "]+")

def distance(w1, w2):
    result = 0

    w1_vowels = list(filter(None, re_consonants.split(w1)))
    w2_vowels = list(filter(None, re_consonants.split(w2)))

    for i in range(min(len(w1_vowels), len(w2_vowels))):
        result += vowel_distance(w1_vowels[i], w2_vowels[i])

    return result

vowel_graph = Graph()
vowel_graph.add_nodes_from(vowels)
vowel_graph.add_edge("a", "e")
vowel_graph.add_edge("e", "i")
vowel_graph.add_edge("u", "o")
vowel_graph.add_edge("u", "i")
vowel_graph.add_edge("e", "o")


INFINITE_DISTANCE = 10

def vowel_distance(v1, v2):
    if has_path(vowel_graph, v1, v2):
        return shortest_path_length(vowel_graph, v1, v2)
    else:
        return INFINITE_DISTANCE



print(distance("faker", "bucker"))
