from collections import defaultdict
from nltk.tokenize import sent_tokenize
from Evaluation import text_measures as tm, POSTagging as pt
import os, random
import re

class Punctuation(object):
    punctuation = defaultdict(dict)
    prepositions = []

    sys_random = {}

    def __init__(self, **kwargs):
        self.sys_random =  random.SystemRandom( os.urandom(2))
        self.punctuation = [',', ':', ';']
        with open('./Dictionaries/prepositions.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                self.prepositions.append(x)

    def clear_punctuation(self, text, punct):
        return text.replace(punct, '')

    def clear_all_punctuation(self, text, change_rate):
        change_rate = change_rate * 150

        for p in self.punctuation:
            rnd = random.randint(0, 100) < change_rate
            if rnd:
                text = self.clear_punctuation(text, p)
        return text

    """
    Insert random punctuation - comma or semicolon before a preposition
    """
    def insert_random(self, text, change_rate):
        change_rate = change_rate * 150
        sentences = sent_tokenize(text)
        result = []
        for sentence in sentences:
            pos_tagged = pt.pos_tag(sentence)            
            # Insert random comma or semicolon before prepositions            
            for index, tagged_word in enumerate(pos_tagged):
                rnd = random.randint(0, 100) < change_rate
                if index > 0 and rnd and tagged_word[0].lower() in self.prepositions:
                    random_punct = self.sys_random.choice([',', ';', ',', ','])
                    result.append((random_punct, '.'))
                result.append(tagged_word)

        return pt.pos_tagged_sentence_to_string(result)

    def insert_redundant_symbols(self, text, change_rate):
        change_rate = change_rate * 150
        exclamationPunct = ['!!', '!', '!!!']
        questionPunct = ['???', '?', '??', '?!?', '!?!']
        rnd = random.randint(0,100) < change_rate
        if rnd:
            text = text.replace('!',  self.sys_random.choice(exclamationPunct))
            text = text.replace('?', self.sys_random.choice(questionPunct))
        return text