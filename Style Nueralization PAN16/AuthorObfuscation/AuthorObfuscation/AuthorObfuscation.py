from ObfuscatrionMethods import Spellcheck as SpellChecker
from ObfuscatrionMethods import ErrorCreator, Punctuation, BritishAmericanNormalization, FillerWords, SymbolReplacement, ParaphraseCorpus
from Evaluation import *
import sys, os
import input_reader, text_utils, output_writer, obfuscator
import nltk

def main(argv):
   nltk.data.path.append('./nltk_data/')
   input_dir, output_dir = input_reader.read_input_and_output_dir(argv)
   print('Input file is: ' + input_dir)
   print('Output file is: ' + output_dir)
   obfuscate_and_save_all_files(input_dir, output_dir)

def obfuscate_and_save_all_files(input_dir, output_dir):
   print('Parsing input...')

   helpers = {
      'stopwords': StopWords(),
      'spellcheck': SpellChecker(), # It seems there is a name clash with another module, so needed to be renamed for this file
      'errorCreator': ErrorCreator(),
      'punctuation': Punctuation(),
      'britishToAmerican': BritishAmericanNormalization(),
      'fillerWords': FillerWords(),
      'symbolReplacement': SymbolReplacement(),
      'paraphraseCorpus': ParaphraseCorpus()
   }

   # Make sure the given output directory exists
   output_writer.ensure_directory_exists(output_dir)
   # Read all files in the given directory and for each execute obfuscation
   for dir_name in os.listdir(input_dir):
      if dir_name[0] != '.': #skip hidden files and folders
        print(dir_name)
        obfuscate_and_save_file(input_dir + '/' + dir_name + '/original.txt', dir_name, output_dir, helpers)

def obfuscate_and_save_file(input_file_path, dir_name, output_dir, helpers):
   print('Obfuscating file ' + input_file_path)
   # Read the input text
   input_text = input_reader.read_input_file(input_file_path)
   # Get array of split parts of the input text
   file_parts = text_utils.split_text(input_text)
   file_parts = obfuscator.obfuscate_all(input_text, file_parts, helpers)   
   output_writer.ensure_directory_exists(output_dir + '/' + dir_name)
   output_file = output_dir + '/' + dir_name + '/obfuscation.json'
   print('Output: ' + output_file)
   output_writer.write_output_file(output_file, file_parts)

if __name__ == "__main__":
   main(sys.argv[1:])
