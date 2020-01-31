from collections import defaultdict
from nltk.tokenize import sent_tokenize
from Evaluation import text_measures as tm
import random, re, text_utils


class FillerWords(object):
    filler_words = []

    def __init__(self, **kwargs):
        with open('./Dictionaries/discourse_markers.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                self.filler_words.append(x)

    # If the sentence starts with a filler word, remove it
    # If clear_inside_sentence is given - clear also such words inside the sentence
    # If split_sentence is set - split the sentence in two at the position of this word
    def clear_filler_words(self, text, clear_inside_sentence, split_sentence):
        sentences = sent_tokenize(text)
        for sentence in sentences:
            changed_sentence = sentence
            for fw in self.filler_words:
                if sentence.lower().startswith(fw):                
                    changed_sentence = re.sub(fw, '', sentence, flags=re.IGNORECASE)
            if clear_inside_sentence and any(fw in sentence.lower() for fw in self.filler_words):
                for fw in self.filler_words:                       
                    changed_sentence = re.sub(fw, '.' if split_sentence else '', changed_sentence, flags=re.IGNORECASE)
            changed_sentence = text_utils.turn_first_char_uppercase(changed_sentence)

            text = text.replace(sentence, changed_sentence)
        return text

    def insert_random(self, text):
        sentences = sent_tokenize(text)
        for sentence in sentences:        
            #changeRatePecents = changeRate * 100
            #rnd = random.randint(0, 100) < changeRatePecents
            rnd = random.choice([False, True])
            if rnd:
                changed_sentence = random.choice(self.filler_words) + ' ' + sentence
                changed_sentence = text_utils.turn_first_char_uppercase(changed_sentence)
                text = text.replace(sentence, changed_sentence)
        return text