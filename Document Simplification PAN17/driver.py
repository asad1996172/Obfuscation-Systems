import obfuscator
import utils
import json
import pickle
import os


contractions = utils.load_pickle_dict('contraction_extraction')
discourse_markers = utils.load_pickle_list('discourse_markers')

experiment_test_file_path = '../prepared_datasets/blogs_10/experiment_5/X_test.pickle'
with open(experiment_test_file_path, 'rb') as handle:
    x_test = pickle.load(handle)


for index, (file_path, file_name, author_id, author, input_text) in enumerate(x_test):
    print('Obfuscating file {} Total Done {} / {}'.format(file_name, index, len(x_test)))

    if not os.path.exists('Obfuscated/blogs_10/' + file_name.split('.')[0]):
        os.makedirs('Obfuscated/blogs_10/' + file_name.split('.')[0])

    meta_data = {}

    meta_data['author_name'] = author
    meta_data['experiment_number'] = 5
    meta_data['is_this_experiment_included_for_obfuscation_detection'] = 1

    meta_data['original'] = None
    meta_data['obfuscated'] = 1
    meta_data['evaded'] = None

    meta_data['included_in_attribution_train'] = 0
    meta_data['included_in_attribution_test'] = 1

    meta_data['included_in_obfuscation_detection_train'] = None
    meta_data['included_in_obfuscation_detection_test'] = None

    with open('Obfuscated/blogs_10/' + file_name.split('.')[0] + '/meta_information.json', 'w') as fp:
        json.dump(meta_data, fp, indent=4)

    output_text = obfuscator.obfuscate_text(input_text, contractions, discourse_markers)

    obfuscated_text_file = open('Obfuscated/blogs_10/' + file_name.split('.')[0] + '/' + file_name, "w")
    obfuscated_text_file.write(output_text)
    obfuscated_text_file.close()
