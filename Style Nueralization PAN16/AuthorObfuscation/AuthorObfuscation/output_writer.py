import os, json

def write_output_file(output_file, text_parts):
   print('Writing output to ' + output_file)

   result_json = []

   for obfuscation in text_parts:
      result_json.append({
         "original": obfuscation.original_text,
         "original-start-charpos": obfuscation.start_pos,
         "original-end-charpos": obfuscation.end_pos,
         "obfuscation": obfuscation.obfuscated_text,
         "obfuscation-id": obfuscation.id
         })

   with open(output_file, 'a+', encoding='utf-8') as outfile:
      json.dump(result_json, outfile, sort_keys=True, indent=2)

   print('Output written.')

def ensure_directory_exists(dir_path):
   # If the given directory does not exist - create it
   if not os.path.exists(dir_path):
      print("Creating directory:" + dir_path)
      os.makedirs(dir_path)

def write_text_to_file(text, file_path):
   with open(file_path, 'a+') as f:
      f.write(text)
