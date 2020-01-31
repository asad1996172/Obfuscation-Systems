import text_utils
from Evaluation import POSTagging as pt

def pos_ratio(text):
   if text:
      word_count = text_utils.word_count(text)
      pos_tagged = pt.pos_tag(text)
      noun_count = 0
      verb_count = 0
      adj_count = 0
      adv_count = 0
      punctuation_count = 0

      for tagged_word in pos_tagged:
         word = tagged_word[0]
         pos = tagged_word[1]
         if pos == 'NOUN':
            noun_count = noun_count + 1
         elif pos == 'VERB':
            verb_count = verb_count + 1
         elif pos == 'ADJ':
            adj_count = adj_count + 1
         elif pos == 'ADV':
            adv_count = adv_count + 1
         elif pos == '.':
            punctuation_count = punctuation_count + 1

      return {
         'NOUN' : noun_count/word_count,
         'VERB' : verb_count/word_count,
         'ADJ' : adj_count/word_count,
         'ADV' : adv_count/word_count,
         'PUNCT' : punctuation_count/word_count,
      }
   else:
      return 0
