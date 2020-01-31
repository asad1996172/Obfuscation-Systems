# -*- coding: utf-8 -*-

from Evaluation import text_measures as tm
import random

def switch(text, changeRate):
    unidict = {k.encode('utf8'): v.encode('utf8') for k, v in latinToCyrilic.items()}
    wordList = tm.words(text)
    for n,w in enumerate(wordList):
        changeRatePecents = changeRate * 100
        rnd = random.randint(0, 100) < changeRatePecents
        if rnd:
            newWord = w
            for l in unidict:
                newWord = newWord.replace(l, unidict[l].decode())
            wordList[n] = newWord
    return ' '.join(wordList)

latinToCyrilic =   {
                'a': '?',
                'A': '?',
                'o': '?',
                'O': '?',
                'e': '?',
                'E': '?',
                'c': '?',
                'C': '?',
                'x': '?',
                'X': '?',
                'p': '?',
                'P': '?',
                'k': '?',
                'K': '?',
                'H': '?',
                'B': '?',
            }