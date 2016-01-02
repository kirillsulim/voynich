

def text_distance(text_words, sample_words, distance_function):
    distance = 0

    for tw in text_words:
        min_distance = 999
        for sw in sample_words:
            dd = distance_function(tw, sw)
            if dd < min_distance:
                min_distance = dd

        distance += min_distance

    return distance