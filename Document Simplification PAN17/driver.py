import obfuscator
import utils
import sys


input_text = utils.get_text('aa_01_1.txt')

contractions = utils.load_pickle_dict('contraction_extraction')
discourse_markers = utils.load_pickle_list('discourse_markers')

output_text = obfuscator.obfuscate_text(input_text, contractions, discourse_markers)
print(output_text)