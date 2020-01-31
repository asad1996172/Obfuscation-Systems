from nltk.corpus import wordnet as wn
from nltk.sentiment import *
from Evaluation import POSTagging as pt
import random
from Evaluation import text_measures as tm
#from ObfuscatrionMethods import 

# Replace some of the nouns, verbs or adjectives with hypernims or synonims
def replace_most_used_words(text, wordCount, changeRate, mostUsedWords=None):
    result = []
    # As very little words were replaced in the experiments, increase the change rate
    changeRatePercents = changeRate * 100 #* 1.5 

    pos_tagged = pt.pos_tag(text)
    for tagged_word in pos_tagged:
        word = tagged_word[0]
        pos_tag = tagged_word[1]
        rnd = random.randint(0, 100) < changeRatePercents
        rnd50 = random.choice([True, False])

        # Replace the most common words with probability of 50% instead of the given change rate
        replace = (rnd50 and mostUsedWords and word in mostUsedWords) or rnd
        
        if replace and pos_tag in ('VERB', 'NOUN', 'ADJ', 'ADV') and wordCount[word] > 3:
            #print('Replacing common word: ' + word + ' rate: ' + str(changeRate))
            new_word = get_most_plausible_synonim(word, pos_tag)
            if new_word == word: new_word = get_hypernim(word, pos_tag)
            result.append((new_word, pos_tag))
        else:
            result.append(tagged_word)
    return pt.pos_tagged_sentence_to_string(result)


# Replace rare words with definitions
def replace_rare_words(text, wordCount, changeRate):
    result = []
    changeRatePercents = changeRate * 100
    pos_tagged = pt.pos_tag(text)
    for tagged_word in pos_tagged:
        word = tagged_word[0]
        pos_tag = tagged_word[1]
        rnd = random.randint(0, 100) < changeRatePercents
        if rnd and pos_tag in ('VERB', 'NOUN', 'ADJ', 'ADV') and wordCount[word] == 1:
            #print('Replacing rare word: ' + word + ' rate: ' + str(changeRate))
            new_word = get_definition(word, pos_tag)
            result.append((new_word, pos_tag))
        else:
            result.append(tagged_word)
    return pt.pos_tagged_sentence_to_string(result)


#be cautions may return different form of the word
def get_most_plausible_synonim(word, posTag):
    if posTag not in ['ADJ', 'ADJ_SAT', 'ADV', 'NOUN', 'VERB']:
        return word
    if posTag == 'NOUN':
        posTag = 'n'
    if posTag == 'VERB':
        posTag = 'v'

    t = wn.synsets(word);
    syns = list(filter(lambda x: str(x._pos) == posTag , t ))
    if syns and len(syns) > 0:
        difSyns = list(filter(lambda x : str(x.lemma_names()[0]) != word and str(x.lemma_names()[0]).find('_') == -1, syns))
        if difSyns and difSyns[0].lemma_names():
            return difSyns[0].lemma_names()[0]
    return word

def get_most_plausible_synonim(word, posTag):
    difSyns = get_synsets_by_pos(word, posTag)
    if difSyns and difSyns[0].lemma_names():
        return difSyns[0].lemma_names()[0]
    return word

def get_definition(word, posTag):
    difSyns = get_synsets_by_pos(word, posTag)
    if difSyns and difSyns[0].definition():
        return difSyns[0].definition()
    return word

def get_synsets_by_pos(word, posTag):
    if posTag not in ['ADJ', 'ADJ_SAT', 'ADV', 'NOUN', 'VERB']:
        return None
    if posTag == 'NOUN':
        posTag = 'n'
    if posTag == 'VERB':
        posTag = 'v'
    if posTag == 'ADJ_SAT':
        posTag = 's'
    if posTag == 'ADV':
        posTag = 'r'
    if posTag == 'ADJ':
        posTag = 'a'
    #todo temp solution

    result = list()
    t = wn.synsets(word)
    syns = [ el for el in t if str(el._pos) == posTag ]
    if syns and len(syns) > 0:
        filtr = [ fl for fl in syns if str(fl.lemma_names()[0]) != word and str(fl.lemma_names()[0]).find('_') == -1 ]
        result.extend(filtr)
        return result
    return None # If not synsets are found

def get_hypernim(word, posTag='NOUN'):
    wordSynset = get_synsets_by_pos(word, posTag)
    if wordSynset:
        hypernim = wordSynset[0].hypernyms()
        if hypernim and hypernim[0] and hypernim[0].lemma_names():
            return hypernim[0].lemma_names()[0]
    return word

def get_hyponym(word, posTag='NOUN'):
    wordSynset = get_synsets_by_pos(word, posTag)
    if wordSynset:
        hyponim = wordSynset[0].hyponyms()
        if hyponim and hyponim[0] and hyponim[0].lemma_names():
            return hyponim[0].lemma_names()[0]
    return word

def replace_setniment(text):
    result = []
    s = SentimentIntensityAnalyzer()
    lexicon = s.make_lex_dict()


    pos_tagged = pt.pos_tag(text)
    for n,w in enumerate(pos_tagged):
        word = w[0]
        pos_tag = w[1]
        newWord = word
        if lexicon.get(word):
            score = lexicon[word]
            syns = get_synsets_by_pos(word, pos_tag)
            if not syns:
                result.append((newWord, pos_tag)) 
                continue
            if score >= 1.5:
                for x in syns:
                    lemma = x.lemma_names()[0]
                    if lemma and lexicon.get(lemma) and lexicon[lemma] < score and lexicon[lemma] > 0:
                            score = lexicon[lemma]  
                            newWord = lemma  

            if score <= -1.5:
                 for x in syns:
                    lemma = x.lemma_names()[0]
                    if lemma and lexicon.get(lemma) and lexicon[lemma] > score and lexicon[lemma] < 0:
                            score = lexicon[lemma]  
                            newWord = lemma 
        result.append((newWord, pos_tag))

    return pt.pos_tagged_sentence_to_string(result)