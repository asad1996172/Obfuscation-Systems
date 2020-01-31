import random, re
from nltk.tokenize import sent_tokenize
from Evaluation import POSTagging as pt
import text_utils

'''
Accepts as parameter text which could contain more than one sentence.
Returns text which merges all or some of the sentences.
'''
def merge_sentences(text,merge_all=True):
   sentences = sent_tokenize(text)
   # If there is only one sentence - return it without modifications
   if len(sentences) < 2:
      return text

   result = ''
   prev_edited = False
   for index, sentence in enumerate(sentences):
      # If previous sentence was edited, start current one with lower case 
      if prev_edited:
         sentence = text_utils.turn_first_char_lowercase(sentence)

      # If merge is required for current pair - replace the ending char
      # with randomly selected separators
      if (merge_all or random.choice([True, False])) and index < len(sentences)-1:
         random_punct = random.choice([',', ';'])
         random_conj = random.choice([' and', ' and', ' and', ' and', '', '', '', ' as', ' yet'])
         sentence = text_utils.replace_last_char(sentence, random_punct + random_conj)
         prev_edited = True
      else:
         prev_edited = False

      if len(result) > 0:
         result = result + ' '
      result = result + sentence

   result = re.sub(r'\n+', r'\n', result)
   return result



'''
Accepts as parameter list with pos tagged words of a sentence.
Returns as text the sentence split in several sentences.
'''
def split_sentence(pos_tagged_sentence):
   result_pos_tagged = []

   has_noun = False
   has_verb = False
   capitalize_next = False

   for tagged_word in pos_tagged_sentence:
      word = tagged_word[0]
      pos = tagged_word[1]

      if capitalize_next:
         tagged_word = (text_utils.turn_first_char_uppercase(word), pos)

      if pos == 'NOUN': has_noun = True
      if pos == 'VERB': has_verb = True
      if pos == 'CONJ' and word.lower() == 'and' and has_noun and has_verb:
         # There was a noun and a verb before 'and',
         # split the sentence here
         result_pos_tagged.append(('.', '.'))
         has_noun = False
         has_verb = False
         capitalize_next = True
      else:
         result_pos_tagged.append(tagged_word)
         capitalize_next = False

   return pt.pos_tagged_sentence_to_string(result_pos_tagged)


'''
POS Tags and splits the text.
'''
def pos_tag_and_split_sentences(text):
   pos_tagged = pt.pos_tag(text)
   return split_sentence(pos_tagged)
