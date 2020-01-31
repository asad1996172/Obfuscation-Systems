'''
Contains constants with avereage statistics of documents.

The stats are taken as the average between the train corpus stats and the file big.txt
where their values were close.

For values which differ a lot (unique and misspelled words ratio) 
the values are taken from the train corpus only.

'''

## AMT ##

SENTENCE_LENGTH = 24
UNIQUE_W0RDS_RATIO = 0.52
MISSPELLED_WORDS_RATIO = 0.43 # Those are words which are not present in file big.txt
NOUN_RATE = 0.30
VERB_RATE = 0.18
ADJ_RATE = 0.092
ADV_RATE = 0.056
PUNCT_RATE = 0.11
STOPWORDS_RATE = 0.47
WORDS_ALL_CAPITAL_LETTERS_RATIO = 0.012
WORDS_FIRST_CAPITAL_LETTER_RATIO = 0.11

EVALUATION_MEASURES = {
    'average_sentence_length': SENTENCE_LENGTH,
    'unique_words_ratio': UNIQUE_W0RDS_RATIO,
    'misspelled_words_rate': MISSPELLED_WORDS_RATIO,
    'average_noun_rate': NOUN_RATE,
    'average_verb_rate': VERB_RATE,
    'average_adj_rate': ADV_RATE,
    'average_adv_rate': ADJ_RATE,
    'average_punct_rate': PUNCT_RATE,
    'stop_words_ratio': STOPWORDS_RATE,
    'words_all_capital_letters_ratio': WORDS_ALL_CAPITAL_LETTERS_RATIO
}

def print_averages():
    print("Average stats from the train corpus and big.txt:")
    print("average_sentence_length = " + str(SENTENCE_LENGTH))
    print("unique_words_ratio = " + str(UNIQUE_W0RDS_RATIO))
    print("misspelled_words_rate = " + str(MISSPELLED_WORDS_RATIO))
    print("average_noun_rate = " + str(NOUN_RATE))
    print("average_verb_rate = " + str(VERB_RATE))
    print("average_adj_rate = " + str(ADJ_RATE))
    print("average_adv_rate = " + str(ADV_RATE))
    print("average_punct_rate = " + str(PUNCT_RATE))
    print("stop_words_ratio = " + str(STOPWORDS_RATE))
    print("first_capital_letter_ratio = " + str(WORDS_FIRST_CAPITAL_LETTER_RATIO))
    print("all_capital_letters_ratio = " + str(WORDS_ALL_CAPITAL_LETTERS_RATIO))