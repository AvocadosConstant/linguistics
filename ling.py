import re

class Corpus:

    def __init__(self, raw):
        self.raw = raw
        self.words = self.parse_raw_corpus(raw)

    def parse_raw_corpus(self, raw):
        """ Extract all ipa (surrounded by square brackets) """
        words = re.findall('\[.*?\]', raw)
        words = list(map(lambda w: w.replace('[', '#'), words))
        words = list(map(lambda w: w.replace(']', '#'), words))
        return words

    def phone_context(self, phone):
        contexts = [word[i-1] + '_' + word[i+1]
                       for word in self.words
                           for i, l in enumerate(word)
                               if l is phone]
        return sorted(set(contexts))
