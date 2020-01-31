import input_reader, output_writer
import json, sys, os, csv, math
from Evaluation import DocumentStats, StopWords, AverageStats, similarity
from ObfuscatrionMethods import Spellcheck
from collections import defaultdict

def main(argv):
    input_dir, output_dir = input_reader.read_input_and_output_dir(argv)
    print('Input dir is: ' + input_dir)
    print('Output dir is: ' + output_dir)
    includeSemanticSimilarity = False #input_reader.check_include_semantic_similarity(argv)
    #save_stats_for_all_files(input_dir, output_dir)
    evaluate_and_save_stats_all_files(input_dir, output_dir, includeSemanticSimilarity)


def save_stats_for_all_files(input_dir, output_dir):
    # Make sure the given output directory exists
    output_writer.ensure_directory_exists(output_dir)
    # Create helper objects in order to not create them for every file
    helpers = {
        'spellcheck': Spellcheck(),
        'stopwords': StopWords()
    }
    # Read all files in the given directory and save stats in one file
    with open(output_dir + '\stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['filename', 'attr_name', 'original', 'obfuscated', 'change', 'change_rate', 'average'])
        for file_name in os.listdir(input_dir):
            print(file_name)
            doc_stats = get_document_stats(input_dir + '/' + file_name, helpers)
            original_stats = doc_stats[0]
            obfuscation_stats = doc_stats[1]
            for attr_name, average_value in AverageStats.EVALUATION_MEASURES.items():
                orig = getattr(original_stats, attr_name)
                obf = getattr(obfuscation_stats, attr_name)
                change = obf - orig
                change_rate = change/orig
                csv_writer.writerow([file_name, attr_name, str(orig), str(obf), str(change), str(change_rate), str(average_value)])


def evaluate_and_save_stats_all_files(input_dir, output_dir, includeSemanticSimilarity):
    # Make sure the given output directory exists
    output_writer.ensure_directory_exists(output_dir)
    # Create helper objects in order to not create them for every file
    helpers = {
        'spellcheck': Spellcheck(),
        'stopwords': StopWords()
    }
    for file_name in os.listdir(input_dir):
        evaluate_and_save_stats(input_dir+'/'+file_name+'/obfuscation.json', file_name, output_dir, helpers, includeSemanticSimilarity)


def evaluate_and_save_stats(input_file, file_name, output_dir, helpers, includeSemanticSimilarity):
    measures = defaultdict(dict)
    data = ''
    with open(input_file) as data_file:    
        data = json.load(data_file)
    stopwords = helpers['stopwords']
    spellcheck = helpers['spellcheck']
    texts = merge_texts(data)
    original_text = texts[0]
    obfuscated_text = texts[1]
    document_stats_original = DocumentStats(original_text, spellcheck, stopwords)
    document_stats_obfuscation = DocumentStats(obfuscated_text, spellcheck, stopwords)
    
    measures['safety_sentenceLengthChange'] = measure_rate_change(document_stats_original.average_sentence_length, document_stats_obfuscation.average_sentence_length)
    measures['safety_nounRateChange'] = measure_rate_change(document_stats_original.average_noun_rate, document_stats_obfuscation.average_noun_rate)
    measures['safety_verbRateChange'] = measure_rate_change(document_stats_original.average_verb_rate, document_stats_obfuscation.average_verb_rate)
    measures['safety_adjectivesRateChange'] = measure_rate_change(document_stats_original.average_adj_rate, document_stats_obfuscation.average_adj_rate)
    measures['safety_adverbsRateChange'] = measure_rate_change(document_stats_original.average_adv_rate, document_stats_obfuscation.average_adv_rate)
    measures['safety_punctuationRateChange'] = measure_rate_change(document_stats_original.average_punct_rate, document_stats_obfuscation.average_punct_rate)
    measures['safety_stopWordsRateChange'] = measure_rate_change(document_stats_original.stop_words_ratio, document_stats_obfuscation.stop_words_ratio)
    measures['safety_uniqueWordsRateChange'] = measure_rate_change(document_stats_original.unique_words_ratio, document_stats_obfuscation.unique_words_ratio)
    measures['safety_capitalizedWordsRateChange'] = measure_rate_change(document_stats_original.words_all_capital_letters_ratio, document_stats_obfuscation.words_all_capital_letters_ratio)
    measures['safety_sequenceDistance'] = similarity.simple_distance(original_text, obfuscated_text)

    if includeSemanticSimilarity:
        measures['soundness_semanticSimilarity'] = average_semantic_similarity(data)

    for key, value in measures.items():
        measure = \
        'measure {\n' + \
        '  key  : "' + str(key) + '"\n' + \
        '  value: "' + str(math.fabs(round(value, 4))) + '"\n' + \
        '}\n'
        #print(measure)
        output_writer.ensure_directory_exists(output_dir + '/' + file_name)
        output_writer.write_text_to_file(measure, output_dir + '/' + file_name + '/evaluation_result.txt')
        #print('File written: ' + output_dir + '/' + file_name + '.txt')

    
def measure_rate_change(val1, val2):
    if (val1 != 0):
        return (val2 - val1)/val1
    else:
        return 0


def get_document_stats(input_file, helpers):
    data = ''
    with open(input_file) as data_file:    
        data = json.load(data_file)
    stopwords = helpers['stopwords']
    spellcheck = helpers['spellcheck']
    texts = merge_texts(data)
    document_stats_original = DocumentStats(texts[0], spellcheck, stopwords)
    document_stats_obfuscation = DocumentStats(texts[1], spellcheck, stopwords)
    return [document_stats_original, document_stats_obfuscation]


def merge_texts(data):
    # Turn the data into dictionary with keys = obfuscation_id and value = the obfuscation object
    data_dict = {}
    for data_part in data:
        data_dict[data_part['obfuscation-id']] = data_part

    original_text = ''
    obfuscated_text = ''
    sorted_keys = sorted(data_dict.keys())
    for obfuscation_id in sorted_keys:
        original_text = original_text + data_dict[obfuscation_id]['original']
        obfuscated_text = obfuscated_text + data_dict[obfuscation_id]['obfuscation']

    return [original_text, obfuscated_text]


def save_stats_comparison(original_stats, obfuscation_stats, output_dir, file_name):
    with open(output_dir+'\\' + file_name + '-stats.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['filename', 'attr_name', 'original', 'obfuscated', 'average'])
        for attr_name, average_value in AverageStats.EVALUATION_MEASURES.items():
            csv_writer.writerow([file_name, attr_name, str(getattr(original_stats, attr_name)), str(getattr(obfuscation_stats, attr_name)), str(average_value)])

    
# def eval_row(original_stats, obfuscation_stats, attr_name, average_value):
#     return [attr_name, str(getattr(original_stats, attr_name)), str(getattr(obfuscation_stats, attr_name)), str(average_value)]

def average_semantic_similarity(data):
    similarity_sum = 0
    count = 0
    for text_part in data:
        sim = similarity.sentence_similarity(text_part['original'], text_part['obfuscation'], True)
        similarity_sum = similarity_sum + sim
        count = count + 1
    return similarity_sum/count


if __name__ == "__main__":
   main(sys.argv[1:])
