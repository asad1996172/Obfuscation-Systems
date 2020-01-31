from collections import defaultdict
from nltk.tokenize import sent_tokenize
from Evaluation import text_measures as tm, POSTagging as pt
import random, re

class SymbolReplacement(object):
    symbols = defaultdict(dict)

    def __init__(self, **kwargs):
        with open('./Dictionaries/symbols.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                split = x.split(' - ')
                self.symbols[split[0]] = split[1]
    
    def replace_symbols(self, text):
        rnd = random.choice([True, False])
        pos_tagged = pt.pos_tag(text)
        result = []
        for n, tagged_word in enumerate(pos_tagged):
            changed = False
            newWord = tagged_word[0].lower()
            if newWord in self.symbols:
                # rnd = random.choice([True, False])
                # if rnd:
                #print('---------CHANGED SYMBOLS---' + newWord + '----------')
                changed = True
                newWord = self.symbols[newWord]
                result.append((newWord, tagged_word[1]))

            if not changed:
                result.append(tagged_word)
                        
        return pt.pos_tagged_sentence_to_string(result)
       