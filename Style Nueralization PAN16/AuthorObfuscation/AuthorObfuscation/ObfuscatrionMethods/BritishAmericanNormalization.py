from collections import defaultdict
from Evaluation import text_measures as tm, POSTagging as pt
import random


class BritishAmericanNormalization(object):
    britishToAmerican = defaultdict(dict)
    americanToBritish = defaultdict(dict)

    def __init__(self, **kwargs):
        with open('./Dictionaries/BritishToAmerican.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                split = x.split(',')
                self.britishToAmerican[split[0]] = split[1]
                self.americanToBritish[split[1]] = split[0]

    def create_errors(self, text):
        pos_tagged = pt.pos_tag(text)
        result = []
        for n, tagged_word in enumerate(pos_tagged):
            changed = False
            newWord = tagged_word[0].lower()
            if newWord in self.britishToAmerican:
                rnd = random.choice([True, False])
                if rnd:
                    changed = True
                    newWord = self.britishToAmerican[newWord]
                    result.append((newWord, tagged_word[1]))

            if newWord in self.americanToBritish:
                rnd = random.choice([True, False])
                if rnd:
                    changed = True
                    newWord = self.americanToBritish[newWord]
                    result.append((newWord, tagged_word[1]))

            if not changed:
                result.append(tagged_word)
                        
        return pt.pos_tagged_sentence_to_string(result)