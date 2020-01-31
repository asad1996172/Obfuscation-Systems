from Evaluation import POSTagging as pt
import re, random

'''
Removes the adjectives and adverbs from sentence.
Parameters:
pos_tagged_sentence - the list with pos-tagged words of the sentence to be processed
leave_one - if True  - one adjective or adverb will be left if there is a sequence of more
          - if False - all adjectives or adverbs are removed before NOUN or VERB
                     - when other POS - one is left (otherwise meaning is lost)

'''
def remove_all_adjectives(text, changeRate, remove_pos_tag='ADJ', next_pos_tag='NOUN',leave_one=False):
    '''
    Remove all adjectives in the text.
    Find a sequence of adjectives and remove them and their connecting words.
    If the adjectives sequence was the end of the sentence, leave one of them.
    '''
    changeRatePercents = changeRate * 100
    rnd = random.randint(0, 100) < changeRatePercents
    if not rnd:
        # Do not transform the text if the adjectives should not be removed
        return text
        
    result = []
    first_adjective_from_sequence = ()
    non_adj_word_from_sequence = ()

    pos_tagged_sentence = pt.pos_tag(text)

    for tagged_word in pos_tagged_sentence:
        word = tagged_word[0]
        pos_type = tagged_word[1]
        if pos_type in [remove_pos_tag] and word != 'not' and word != "n't" and not (word.startswith('wh')): #and len(first_adjective_from_sequence) <= 0:
            first_adjective_from_sequence = tagged_word
        elif pos_type == 'CONJ' and word == 'and':
            non_adj_word_from_sequence = tagged_word
        elif pos_type in [next_pos_tag]:
            if leave_one and len(first_adjective_from_sequence) > 0:
                result.append(first_adjective_from_sequence)
                if len(non_adj_word_from_sequence) > 0:
                    result.append(non_adj_word_from_sequence)
            result.append(tagged_word)
            first_adjective_from_sequence = ()
            non_adj_word_from_sequence = ()
        elif pos_type not in [remove_pos_tag, next_pos_tag, 'CONJ'] and word != ',':
            if len(first_adjective_from_sequence) > 0:
                # If there is an adjective on the pipe, add it as it would lose the meaning
                # The house was old and the tree was green.                
                result.append(first_adjective_from_sequence)              
                if len(non_adj_word_from_sequence) > 0:
                    result.append(non_adj_word_from_sequence)
            result.append(tagged_word)
            first_adjective_from_sequence = ()
            non_adj_word_from_sequence = ()
        elif pos_type == '.':
            if word in ('.', '?', '!'):
                if len(first_adjective_from_sequence) > 0:
                    # If there is an adjective on the pipe, add it as it would lose the meaning
                    # The house was old and the tree was green.                    
                    result.append(first_adjective_from_sequence)
                    #if len(non_adj_word_from_sequence) > 0:
                    #    result.append(non_adj_word_from_sequence)
                    first_adjective_from_sequence = ()
                    non_adj_word_from_sequence = ()
            result.append(tagged_word)
        else:
            result.append(tagged_word)

    return pt.pos_tagged_sentence_to_string(result)


'''
Sample usage:

from ObfuscatrionMethods import adjectives_transformations as at
from Evaluation import POSTagging as pt
tagged = pt.pos_tag("The big and old or new house was beautifully drawn by the old but still young-souled artist who was happy and cheerful and the birds were singing happy and loudly.")
res = at.remove_all_adjectives(tagged)
pt.pos_tagged_sentence_to_string(res)
res1 = at.remove_all_adjectives(tagged, True)
pt.pos_tagged_sentence_to_string(res1)
'''