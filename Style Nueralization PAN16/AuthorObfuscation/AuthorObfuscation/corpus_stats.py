import sys, os
import input_reader, text_utils, output_writer, obfuscator
import nltk
from ObfuscatrionMethods import Spellcheck
from Evaluation import text_measures, pos_measures, StopWords, DocumentStats, AverageStats

# This file contains measures of the stats of the text corpus in the given input directory'
# (The naming convention of the files is the same as the task input)

def main(argv):
    option = input_reader.read_argument_value(argv, 's')
    input_dir = input_reader.read_input_dir(argv)
    #Possible options: 
    # corpus : -i specifies input directory for corpus
    # dir : -i specifies directory with files to be compared
    if not option: option = 'corpus'
    if option == 'corpus':        
        calc_corpus_stats(input_dir)
    elif option == 'dir':
        compare_stats_for_all_files(input_dir)

def calc_corpus_stats(input_dir):
    average_sentence_length = 0
    sentence_count = 0
    word_count = 0
    unique_words_count = 0
    unique_words_ratio = 0
    files_count = 0    
    misspelled_words_rate = 0
    average_noun_rate = 0
    average_verb_rate = 0
    average_adj_rate = 0
    average_adv_rate = 0
    average_punct_rate = 0
    stop_words_count = 0
    stop_words_ratio = 0
    words_all_capital_letters_ratio = 0
    words_first_capital_letter_ratio = 0

    stopwords = StopWords()
    spellcheck = Spellcheck()

    for dir_name in os.listdir(input_dir):
        all_files = []
        for (_, _, file_names) in os.walk(input_dir + '/' + dir_name):
            all_files.extend(file_names)
            break
        for file in all_files:
            file_content = input_reader.read_input_file(input_dir + '/' + dir_name + '/' + file)
            files_count = files_count + 1
            doc_stats = DocumentStats(file_content, spellcheck, stopwords)

            word_count = word_count + doc_stats.word_count
            sentence_count = sentence_count + doc_stats.sentence_count
            average_sentence_length = average_sentence_length + doc_stats.average_sentence_length
            unique_words_count = unique_words_count + doc_stats.unique_words_count
            unique_words_ratio = unique_words_ratio + doc_stats.unique_words_ratio
            misspelled_words_rate = misspelled_words_rate + doc_stats.misspelled_words_rate
            pos_rate = doc_stats.pos_rate
            average_noun_rate = average_noun_rate + pos_rate['NOUN']
            average_verb_rate = average_verb_rate + pos_rate['VERB']
            average_adj_rate = average_adj_rate + pos_rate['ADJ']
            average_adv_rate = average_adv_rate + pos_rate['ADV']
            average_punct_rate = average_punct_rate + pos_rate['PUNCT']
            stop_words_count = stop_words_count + doc_stats.stop_words_count
            stop_words_ratio = stop_words_ratio + doc_stats.stop_words_ratio
            words_all_capital_letters_ratio = words_all_capital_letters_ratio + doc_stats.words_all_capital_letters_ratio
            words_first_capital_letter_ratio = words_first_capital_letter_ratio + doc_stats.words_first_capital_letter_ratio
            #print(text_measures.count_words(file_content))

    print("Averages for corpus:")
    print("average_sentence_length = " + str(average_sentence_length/files_count))
    print("sentence_count = " + str(sentence_count/files_count))
    print("word_count = " + str(word_count/files_count))
    print("unique_words_count = " + str(unique_words_count/files_count))
    print("unique_words_ratio = " + str(unique_words_ratio/files_count))
    print("misspelled_words_rate = " + str(misspelled_words_rate/files_count))
    print("average_noun_rate = " + str(average_noun_rate/files_count))
    print("average_verb_rate = " + str(average_verb_rate/files_count))
    print("average_adj_rate = " + str(average_adj_rate/files_count))
    print("average_adv_rate = " + str(average_adv_rate/files_count))
    print("average_punct_rate = " + str(average_punct_rate/files_count))
    print("stop_words_count = " + str(stop_words_count/files_count))
    print("stop_words_ratio = " + str(stop_words_ratio/files_count))
    print("words_all_capital_letters_ratio = " + str(words_all_capital_letters_ratio/files_count))
    print("words_first_capital_letter_ratio = " + str(words_first_capital_letter_ratio/files_count))


def compare_stats_for_all_files(input_dir):
    stopwords = StopWords()
    spellcheck = Spellcheck()

    AverageStats.print_averages()

    for dir_name in os.listdir(input_dir):
        file_content = input_reader.read_input_file(input_dir + '/' + dir_name + '/obfuscation.json')
        doc_stats = DocumentStats(file_content, spellcheck, stopwords)
        print('>>>>>>>>>>>> Stats for dir ' + dir_name)
        doc_stats.print_stats()

if __name__ == "__main__":
    main(sys.argv[1:])