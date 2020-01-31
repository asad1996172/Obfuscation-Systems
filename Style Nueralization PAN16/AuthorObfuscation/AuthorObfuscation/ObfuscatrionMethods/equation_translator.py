import re
from Evaluation import text_measures as tm

def detect_equation(text):
    comparingSymbols = re.compile('.[<>=]+.')
    innerSymbols = re.compile('.[\+\-\*\/]+.')
    comp1 = comparingSymbols.findall(text)
    comp2 = innerSymbols.findall(text)
    if comp1 and comp2:
        return True
    return False

def transform_equation(text):
    words = tm.all_symbols_tokenizer(text)
    for n,w in enumerate(words):
        for sym in symbols:
            if sym in w:
                words[n] = words[n].replace(sym, symbols[sym])
    return ' '.join(words)

symbols =   {
                '+': ' plus ',
                '-': ' minus ',
                '*': ' multiplied by ',
                '/': ' divided by ',
                '=': ' equals ',
                '>': ' greather than ',
                '<': ' less than ',
                '<=': ' less than or equal to ',
                '>=': ' greater than or equal to ',
            }