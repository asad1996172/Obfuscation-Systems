# encoding=utf8  
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from TextPart import TextPart

MAX_SEQUENCE_LENGTH = 50

def words(text):
   tokenizer = RegexpTokenizer(r'\w+')
   return tokenizer.tokenize(text)

def word_count(text):
   tokens = words(text)
   return len(tokens)

def split_text(text):
   #text = text.strip() #Probably this was the problem, with the slight length bug. 
   sentences = sent_tokenize(text)

   positioned_sentences = []
   pos = 0
   obfuscation_id = 1
   temp_sequence = ''

   for index, sentence in enumerate(sentences):
      sentence_length = len(sentence)

      if not temp_sequence:
         temp_sequence = sentence
      else:
         if len(sentences) == index+1:
            temp_sequence = temp_sequence + ' ' + sentence
         if word_count(temp_sequence + sentence) > MAX_SEQUENCE_LENGTH or len(sentences) == index+1:
            # Adding the current sequence would exceed the allowed length =>
            # 1. Add the current sequence to the list
            # 2. Reset the sequence with the new sentence
            start_pos = pos
            end_pos = start_pos + len(temp_sequence) + 1 # Add one position for interval
            # Clear the new lines from the text
            temp_sequence = temp_sequence.strip().replace('\n', ' ')
            temp_sequence = temp_sequence + ' ' # Add an interval at the end of the sentence
            text_part = TextPart(obfuscation_id, start_pos, end_pos, temp_sequence)
            positioned_sentences.append(text_part)
            pos = end_pos + 1
            obfuscation_id = obfuscation_id + 1

            # The sentence is starting the new sequence
            temp_sequence = sentence
         else:
            # Still allowed length - add the sentence to the temp sequence and continue
            if temp_sequence:
               temp_sequence = temp_sequence + ' ' + sentence
            else:
               temp_sequence = sentence
  
   return positioned_sentences


def turn_first_char_lowercase(text):
   text = text.strip()
   if text:
      return text.lower()[:1] + text[1:]
   else:
      return ''

def turn_first_char_uppercase(text):
   text = text.strip()
   if text:
      return text.upper()[:1] + text[1:]
   else:
      return ''

def replace_last_char(text, replacement):
   if text:
      if text.endswith(('.', '?', '!')):
         return text[0:(len(text)-1)] + replacement
      else:
         return text
   else:
      return ''