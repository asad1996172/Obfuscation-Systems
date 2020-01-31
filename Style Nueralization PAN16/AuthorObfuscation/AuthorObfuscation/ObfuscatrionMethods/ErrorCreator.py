from collections import defaultdict
from Evaluation import text_measures as tm, POSTagging as pt
import random


class ErrorCreator(object):
    spellingErrorDictionary = defaultdict(dict)

    def __init__(self, **kwargs):
        with open('./Dictionaries/common-mistakes.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                split = x.split('-')
                key = split[0].strip()
                values = list(map(lambda x : x.strip(), split[1].split(',')))
                self.spellingErrorDictionary[key] = values

    def number_of_possible_mistakes(self, text):
        wordList = tm.words(text)
        possibleMistakes = 0
        for w in wordList:
            if w.lower() in self.spellingErrorDictionary:
                possibleMistakes += 1
        return possibleMistakes

    def create_errors(self, text, errorRate):
        wordList = tm.words(text)
        for n,w in enumerate(wordList):
            if w.lower() in self.spellingErrorDictionary:
                changeRatePecents = errorRate * 100
                rnd = random.randint(0, 100) < changeRatePecents
                if rnd:
                    variants = self.spellingErrorDictionary.get(w) 
                    wordList[n] = random.choice(variants)
        return ' '.join(wordList)

    def pos_tag_and_create_errors(self, text, changeRate):
        changeRatePercents = changeRate * 100
        result = []
        pos_tagged = pt.pos_tag(text)
        for tagged_word in pos_tagged:
            if tagged_word[0].lower() in self.spellingErrorDictionary:                
                rnd = random.randint(0, 100) < changeRatePercents
                if rnd:
                    variants = self.spellingErrorDictionary.get(tagged_word[0])
                    if variants:
                        changed_word = (random.choice(variants), tagged_word[1]) 
                        result.append(changed_word)
                    else:
                        result.append(tagged_word)
            else:
                result.append(tagged_word)

        return pt.pos_tagged_sentence_to_string(result)
