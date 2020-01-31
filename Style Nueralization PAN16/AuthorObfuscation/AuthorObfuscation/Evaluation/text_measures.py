# encoding=utf8  
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from TextPart import TextPart
from collections import Counter

def words(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)

def all_symbols_tokenizer(text):
    tokenizer = RegexpTokenizer(r'\S+')
    return tokenizer.tokenize(text)

def word_count(text):
    if text:
        tokens = words(text)
        return len(tokens)
    else:
        return 0

def average_sentence_length(text):
    if text:
        sentences = sent_tokenize(text)
        return word_count(text)/len(sentences)
    else:
        return 0

def sentence_count(text):
    if text:
        sentences = sent_tokenize(text)
        return len(sentences)
    else:
        return 0

def unique_words_count(text):
    if text:
        tokens = words(text)
        unique_words = set(tokens)
        return len(unique_words)
    else:
        return 0

def unique_words_ratio(text):
    return unique_words_count(text)/word_count(text)

def misspelled_words_rate(text, spellcheck):
    if text and spellcheck:
        tokens = words(text)
        return len(spellcheck.known(tokens))/len(tokens)
    else:
        return 0

# Returns an array with numeric values representing 
# average count per sentence of the following:
# [commas, colons, semicolons]
def average_punctuation_count(text):
    sentences = sent_tokenize(text)
    commas_count = 0
    colons_count = 0
    semicolons_count = 0
    for sentence in sentences:
        commas_count = commas_count + sentence.count(',')
        colons_count = colons_count + sentence.count(':')
        semicolons_count = semicolons_count + sentence.count(';')
    return [commas_count, colons_count, semicolons_count]

def count_words(text):
    wds = words(text)
    wordsfrequency = []
    for x in wds:
        wordsfrequency.append(x.lower())
    word_dict = Counter(wordsfrequency)
    return word_dict

def capitalized_words_ratio(text, allLettersCapital=True):
    wds = words(text)
    cap_words_count = 0
    for word in wds:
        if allLettersCapital and word.isupper() or (not allLettersCapital) and word[0].isupper(): 
            cap_words_count = cap_words_count + 1
    return cap_words_count / len(wds)

        
