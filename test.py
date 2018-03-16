from ling import Corpus

# sample of korean words
raw = 'a. [ʃi] poem b. [miʃin] superstition c. [ʃinmun] newspaper d. [tʰaksaŋʃiɡe] table clock e. [ʃilsu] mistake f. [oʃip] fifty g. [paŋʃik] method h. [kanʃik] snack i. [kaʃi] thorn j. [sal] flesh k. [kasu] singer l. [sanmun] prose m. [kasəl] hypothesis n. [miso] smile o. [susek] search p. [tapsa] exploration q. [so] cow '

corpus = Corpus(raw)

for word in corpus.words:
    print(word)

for word in corpus.phone_context('i'):
    print(word)

    """
    context = []
    for word in self.words:
        for i, l in enumerate(word):
            if l is phone:
                context.append(word[i-1:i+1])
    return context
    """
