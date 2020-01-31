import nltk

def pos_tag(text):
    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens, tagset = 'universal')
    return pos

def pos_tagged_sentence_to_string(tagged_sentence_list):
   '''
   Input: [('The', 'DET'), ('house', 'NOUN'), ('is', 'VERB'), ('very', 'ADV'), ('big', 'ADJ'), ('.', '.')]
   Output: 'The house is very big.'
   '''
   return ''.join(map(lambda x: x[0] if x[1] == '.' and x[0] not in ("\'", '(', '[') else ' ' + x[0], tagged_sentence_list))[1:]

