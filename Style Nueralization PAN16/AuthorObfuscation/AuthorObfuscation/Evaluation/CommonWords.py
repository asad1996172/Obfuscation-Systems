import collections

class CommonWords(object):
    dictWords = []

    def __init__(self, **kwargs):
        with open('./Dictionaries/most_common_words.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            self.dictWords = s.splitlines()

    #returns -1 if the word is not in top 10000 used words
    #returns number from 1 to 10000 base on how common the word is 
    #todo some normalization ?
    def word_rank(self, word):
        tp = self.dictWords.count(word)
        if tp > 0:
            return self.dictWords.index(word)
        return -1