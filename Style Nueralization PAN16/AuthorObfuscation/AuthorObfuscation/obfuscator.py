from ObfuscatrionMethods import *
from ObfuscatrionMethods import sentence_transformations, adjectives_transformations, numbers_to_words, uppercase_obfuscation, regex_transformations
from Evaluation import StopWords, DocumentStats, AverageStats, POSTagging as pt
import text_utils, random

def obfuscate_all(original_text, text_parts, helpers):
    document_stats = DocumentStats(original_text, helpers['spellcheck'], helpers['stopwords'])

    for text in text_parts:
        text.obfuscated_text = obfuscate_text(text.original_text, document_stats, helpers)
    return text_parts

def obfuscate_text(text, document_stats, helpers):
    # 1. Apply general transfomations
    text = apply_general_transformations(text, helpers)
    # 2. According to the document measures - apply transformations to get closer to the averages
    text = apply_obfuscation(text, document_stats, helpers)
    # 3. Add noise to the text
    text = add_noise(text, helpers)

    # Add an empty space at the end of the text to make meaningful text when concatenating the output
    text = text + ' '
    
    return text


def apply_obfuscation(text, document_stats, helpers):
    spellchecker = helpers['spellcheck']
    stopwords = helpers['stopwords']
    errorCreator = helpers['errorCreator']
    punctuation = helpers['punctuation']
    fillerWords = helpers['fillerWords']
    paraphraseCorpus = helpers['paraphraseCorpus']

    spell_correction = True 
    obfuscate_stop_words = True
    obfuscate_punctuation = True
    transform_sentences = True
    change_pos_count = False # This does not work very well, especially when sentences are transformed.
    substitute_words = True
    uppercase = True
    paraphrase_corpus = True

    # Obfuscate uppercase words
    if uppercase:
        text = obfuscate_uppercase(text, document_stats)

    # Paraphrasing
    if paraphrase_corpus:
        text = paraphraseCorpus.obfuscate(text)
   
    # Obfuscate stop words
    if obfuscate_stop_words:
        text = obfuscate_stopwords(text, document_stats, stopwords)
        
    # Obfuscate punctuation
    if obfuscate_punctuation:
        text = obfuscate_punctuation_count(text, document_stats, punctuation)
        
    # Remove adjectives
    if change_pos_count:
        #TODO -Georgi: We don't use this for now, but we should re-do this to be more effective
        text = obfuscate_pos_count(text, document_stats)
    
    # Substitute some words with their synonims, hypernims or definitions
    if substitute_words:
        text = obfuscate_unique_words_count(text, document_stats)

    # Split or merge sentences
    if transform_sentences:
        text = obfuscate_sentence_length(text, document_stats, fillerWords)

    # Use spellchecker    
    if spell_correction:
        text = obfuscate_spelling(text, document_stats, spellchecker, errorCreator)    
    
    return text

def obfuscate_spelling(text, document_stats, spellchecker, errorCreator):
    # If the misspelled words are more than the average - apply spell correction
    # Otherwise - insert common misspellings
    if document_stats.misspelled_words_rate > AverageStats.MISSPELLED_WORDS_RATIO:        
        text = spellchecker.pos_tag_and_correct_text(text)
    else:
        errorRate = AverageStats.MISSPELLED_WORDS_RATIO - document_stats.misspelled_words_rate
        text = errorCreator.pos_tag_and_create_errors(text, errorRate)
    return text

def obfuscate_stopwords(text, document_stats, stopwords):
    change_rate = abs(document_stats.stop_words_ratio - AverageStats.STOPWORDS_RATE)
    text = stopwords.obfuscate(text, change_rate)
    return text

def obfuscate_punctuation_count(text, document_stats, punctuation):
    change_rate = document_stats.average_punct_rate - AverageStats.PUNCT_RATE
    if change_rate > 0:
        text = punctuation.clear_all_punctuation(text, change_rate)
    else:
        change_rate = abs(change_rate)
        text = punctuation.insert_redundant_symbols(text, change_rate)
        text = punctuation.insert_random(text, change_rate)
    return text

def obfuscate_sentence_length(text, document_stats, fillerWords):
    THRESHHOLD = 3 # If difference is no more then 3 words we don't change the sentence length
    diff = document_stats.average_sentence_length - AverageStats.SENTENCE_LENGTH
    if abs(diff) <= THRESHHOLD:
        return text
    if diff > 0:
        text = sentence_transformations.pos_tag_and_split_sentences(text)
        text = fillerWords.clear_filler_words(text, True, True)
    else:
        text = sentence_transformations.merge_sentences(text)
    return text

def obfuscate_pos_count(text, document_stats):
    # We only have removal of adjectives
    if document_stats.average_adj_rate > AverageStats.ADJ_RATE:
        changeRate = document_stats.average_adj_rate - AverageStats.ADJ_RATE
        text = adjectives_transformations.remove_all_adjectives(text, changeRate, 'ADJ', 'NOUN', random.choice([True, False]))
    if document_stats.average_adv_rate > AverageStats.ADV_RATE:
        changeRate = document_stats.average_adv_rate - AverageStats.ADV_RATE
        text = adjectives_transformations.remove_all_adjectives(text, changeRate, 'ADV', 'VERB', True)
    return text

def obfuscate_uppercase(text, document_stats):
    #if document_stats.words_all_capital_letters_ratio > AverageStats.WORDS_ALL_CAPITAL_LETTERS_RATIO:
    text = uppercase_obfuscation.obfuscate_all_uppercase_words(text)
    return text

def obfuscate_unique_words_count(text, document_stats):
    '''
    If the unique word count is above average:
    - replace part of the most used nouns, verbs and adjectives with synonims or hypernims

    If the unique word count is below average:
    - replace with explanation one of the nouns, verbs and adjectives used only once
    '''
    changeRate = document_stats.unique_words_ratio - AverageStats.UNIQUE_W0RDS_RATIO
    if document_stats.unique_words_ratio > AverageStats.UNIQUE_W0RDS_RATIO:
        text = word_substitution.replace_most_used_words(text, document_stats.words_count, changeRate, document_stats.most_used_words)
    else:
        text = word_substitution.replace_rare_words(text, document_stats.words_count, -changeRate)
    return text


def add_noise(text, helpers):
    apply_translation = False # Can be included later.
    british_american = True
    filler_words = True

    # Applying two-way translation obfuscation on the text
    if apply_translation:
        translator = Translation()
        languages = [Language.Croatian, Language.Estonian]
        text = translator.translate(text, languages) 
    
    if british_american:
        britishToAmerican = helpers['britishToAmerican']
        text = britishToAmerican.create_errors(text)

    if filler_words and random.choice([False, False, True, False, False]):
        fillerWords = helpers['fillerWords']
        text = fillerWords.insert_random(text)

    return text


def apply_general_transformations(text, helpers):
    remove_short_forms = True
    replace_numbers = True
    transform_equations = True
    replace_symbols = True
    replace_regex = True

    if replace_regex:
        text = regex_transformations.apply(text)

    if transform_equations and equation_translator.detect_equation(text):
        text = equation_translator.transform_equation(text)

    if replace_numbers:
        text = numbers_to_words.replace_numbers(text)

    if remove_short_forms:
        text = short_forms.replace_short_forms(text)

    if replace_symbols:
        symbolReplacement = helpers['symbolReplacement']
        text = symbolReplacement.replace_symbols(text)
    
    return text