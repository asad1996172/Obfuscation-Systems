from nltk.corpus import stopwords
from Evaluation import text_measures as tm, POSTagging as pt
from collections import Counter
from collections import defaultdict
import random

class StopWords(object):

    stops = []
    stopObfuscation = defaultdict(dict)

    def __init__(self, **kwargs):
        self.stops = set(stopwords.words('english'))
        with open('./Dictionaries/stopwords-obfuscation.txt', 'r', encoding='utf-8') as f:
            s = f.read()
            temp = s.splitlines()
            for x in temp:
                split = x.split('-')
                self.stopObfuscation[split[0].strip()] = split[1].strip()

    def stop_words_sum(self, text):
        wds = tm.words(text)
        count = 0
        for x in wds:
            if x.lower() in self.stops:
                count += 1
        return count

    def stop_words_ratio(self, text):
        return self.stop_words_sum(text)/tm.word_count(text)

    def count_stopwords(self, text):
        wds = tm.words(text)

        stopwordsfrequency = []
        for x in wds:
            if x.lower() in self.stops:
                stopwordsfrequency.append(x.lower())
        word_dict = Counter(stopwordsfrequency)
        return word_dict

    def obfuscate(self, text, change_rate):
        change_rate_percents = change_rate * 150
        pos_tagged = pt.pos_tag(text)
        result = []
        for n, tagged_word in enumerate(pos_tagged):
            new_word = tagged_word[0].lower()
            replaced = False
            if new_word in self.stopObfuscation:
                rnd = random.randint(0, 100) < change_rate_percents
                if rnd:
                    replaced = True
                    new_word = self.stopObfuscation[new_word]
                    if new_word:
                        result.append((new_word, tagged_word[1]))
            if not replaced:
                result.append(tagged_word)
        return pt.pos_tagged_sentence_to_string(result)
