from collections import defaultdict
from Evaluation import text_measures as tm, POSTagging as pt
import random

class ParaphraseCorpus(object):
    obfuscationCorpus = defaultdict(dict)

    def __init__(self, **kwargs):
        with open('./Dictionaries/phrasal-corpus.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                split = x.split(' - ')
                self.obfuscationCorpus[split[0]] = split[1]

    def obfuscate(self, text): #TODO: What should be the change rate ? Now it is effectively 0.5
        if any (w in text for w in self.obfuscationCorpus.keys()):
            for key, value in self.obfuscationCorpus.items():
                if text.find(' ' + key + ' ') > -1:
                    rnd = random.choice([True, False])
                    if rnd:
                        #print('----- Replaced: >' + key + '< with >'+value)
                        text = text.replace(' ' + key + ' ', ' ' + value + ' ')
        return text