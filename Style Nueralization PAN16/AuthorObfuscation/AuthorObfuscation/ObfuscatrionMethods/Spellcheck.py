import re, collections
from Evaluation import POSTagging as pt

def words(text): 
        return re.findall('[a-z]+', text.lower())

def train(features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Spellcheck(object):
    NWORDS = collections.defaultdict(lambda: 1)

    def __init__(self, **kwargs):
        with open('./Dictionaries/big.txt', 'r') as content_file:
            content = content_file.read()
        dictionaryWords = words(content)
        trainingData = train(dictionaryWords) 
        self.NWORDS = trainingData

    def edits1(self, word):
        splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        inserts    = [a + c + b for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self, words): 
        return set(w for w in words if w in self.NWORDS)

    def correct(self, word):
        candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
        return max(candidates, key=self.NWORDS.get)

    def pos_tag_and_correct_text(self, text):
        result = []
        pos_tagged = pt.pos_tag(text)
        for tagged_word in pos_tagged:
            # Do not correct puntuation, numbers and known words
            if tagged_word[1] in ('.', 'NUM') or tagged_word[0].lower() in self.NWORDS or not tagged_word[0].isalnum():
                result.append(tagged_word)
            else:
                result.append((self.correct(tagged_word[0]), tagged_word[1]))

        return pt.pos_tagged_sentence_to_string(result)

            