from nltk.tokenize import sent_tokenize
import nltk
import re
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from pyfreeling import Analyzer

def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .', '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
        "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()


def contraction_replacement(sentence, contractions):
    orig_sentence = sentence

    all_contractions = contractions.keys()
    all_expansions = contractions.values()
    contractions_count = 0
    expansions_count = 0

    for contraction in all_contractions:
        if contraction.lower() in sentence.lower():
            contractions_count += 1
    for expansion in all_expansions:
        if expansion.lower() in sentence.lower():
            expansions_count += 1

    if contractions_count > expansions_count:
        # Replace all contractions with their expansions
        temp_contractions = dict((k.lower(), v) for k, v in contractions.items())
        for contraction in all_contractions:
            if contraction.lower() in sentence.lower():
                case_insesitive = re.compile(re.escape(contraction.lower()), re.IGNORECASE)
                sentence = case_insesitive.sub(temp_contractions[contraction.lower()], sentence)
        contractions_applied = True
    elif expansions_count > contractions_count:
        inv_map = {v: k for k, v in contractions.items()}
        temp_contractions = dict((k.lower(), v) for k, v in inv_map.items())
        for expansion in all_expansions:
            if expansion.lower() in sentence.lower():
                case_insesitive = re.compile(re.escape(expansion.lower()), re.IGNORECASE)
                sentence = case_insesitive.sub(temp_contractions[expansion.lower()], sentence)
        contractions_applied = True
    else:
        contractions_applied = False

    # print("Original:::::", orig_sentence)
    # print("Total Contractions: ", contractions_count)
    # print("Total Expansions: ", expansions_count)
    # print("Obfuscated:::::", sentence)
    # print("============================================")

    return sentence, contractions_applied


def synonym_substitution(sentence, all_words):
    new_tokens = []
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        synset_name = (lesk(sentence, token))
        try:
            synonyms = synset_name.lemma_names()
            print(token, ":::::", synonyms)
            for synonym in synonyms:
                if synonym.lower() not in all_words:
                    token = synonym
                    break
        except Exception as e:
            print(e)
            pass
        new_tokens.append(token)

    final = untokenize(new_tokens)
    final = final.capitalize()
    return final

def obfuscate_text(input_text, contractions, discourse_markers):
    sentences = sent_tokenize(input_text)
    tokens = set(nltk.word_tokenize(input_text.lower()))
    for sentence in sentences:
        sentence = sentence.strip()
        sentence, contractions_applied = contraction_replacement(sentence, contractions)
        if contractions_applied:
            print(sentence)
            sentence = synonym_substitution(sentence, tokens)
            print(sentence)

