

class Translator:
    def __init__(self, from_string, to_string):
        self.dict = dict()

        for i in range(len(from_string)):
            if i < len(to_string):
                self.dict[from_string[i]] = to_string[i]
            else:
                self.dict[from_string[i]] = "?"

    def trans(self, string):
        def conv(char):
            if char in self.dict:
                return self.dict[char]
            else:
                return char

        return "".join([conv(c) for c in string])
