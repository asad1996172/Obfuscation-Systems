from ObfuscatrionMethods import Spellcheck
from Evaluation import text_measures, pos_measures, StopWords

class DocumentStats(object):

    def __init__(self, document_text, spellcheck , stopwords):
        self.word_count = text_measures.word_count(document_text)
        self.sentence_count = text_measures.sentence_count(document_text)
        self.average_sentence_length = text_measures.average_sentence_length(document_text)
        self.unique_words_count = text_measures.unique_words_count(document_text)
        self.unique_words_ratio = text_measures.unique_words_ratio(document_text)
        self.misspelled_words_rate = text_measures.misspelled_words_rate(document_text, spellcheck)
        self.pos_rate = pos_measures.pos_ratio(document_text)
        self.average_noun_rate = self.pos_rate['NOUN']
        self.average_verb_rate = self.pos_rate['VERB']
        self.average_adj_rate = self.pos_rate['ADJ']
        self.average_adv_rate = self.pos_rate['ADV']
        self.average_punct_rate = self.pos_rate['PUNCT']
        self.stop_words_count = stopwords.stop_words_sum(document_text)
        self.stop_words_ratio = stopwords.stop_words_ratio(document_text)
        self.words_count = text_measures.count_words(document_text)
        self.words_first_capital_letter_ratio = text_measures.capitalized_words_ratio(document_text, False)
        self.words_all_capital_letters_ratio = text_measures.capitalized_words_ratio(document_text, True)
        self.most_used_words = list(map(lambda x: x[0], self.words_count.most_common(10)))

    def print_stats(self):
        print("average_sentence_length = " + str(self.average_sentence_length))
        print("sentence_count = " + str(self.sentence_count))
        print("word_count = " + str(self.word_count))
        print("unique_words_count = " + str(self.unique_words_count))
        print("unique_words_ratio = " + str(self.unique_words_ratio))
        print("misspelled_words_rate = " + str(self.misspelled_words_rate))
        print("average_noun_rate = " + str(self.average_noun_rate))
        print("average_verb_rate = " + str(self.average_verb_rate))
        print("average_adj_rate = " + str(self.average_adj_rate))
        print("average_adv_rate = " + str(self.average_adv_rate))
        print("average_punct_rate = " + str(self.average_punct_rate))
        print("stop_words_count = " + str(self.stop_words_count))
        print("stop_words_ratio = " + str(self.stop_words_ratio))
        print("words_first_capital_letter_ratio = " + str(self.words_first_capital_letter_ratio))
        print("words_all_capital_letters_ratio = " + str(self.words_all_capital_letters_ratio))
        print(self.stop_words_count)
        print(self.words_count)
        print(self.most_used_words)