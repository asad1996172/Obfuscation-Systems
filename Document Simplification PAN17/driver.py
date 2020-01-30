import obfuscator
import utils

dummy_text = """I'd like to be there, but I am scared of ghosts. Basically, that's why I didn't stay there. I am going to pay it.
But here we are and, that's not even the worst part.
"""

contractions = utils.load_pickle_dict('contraction_extraction')
discourse_markers = utils.load_pickle_list('discourse_markers')

output_text = obfuscator.obfuscate_text(dummy_text, contractions, discourse_markers)