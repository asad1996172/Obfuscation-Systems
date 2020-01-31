import re, random

def replace_short_forms(text):
   text = replace_short_negation(text)
   text = replace_short_have(text)
   text = replace_short_would_had(text)
   text = replace_short_to_be(text)
   text = replace_short_will(text)
   return text

def replace_short_negation(text):
   text = re.sub("ain't", 'is not', text, flags=re.IGNORECASE)
   return re.sub(r" (.+)n't", r' \1 not', text, flags=re.IGNORECASE)

def replace_short_have(text):
   return re.sub(r" (.+)'ve", r' \1 have', text, flags=re.IGNORECASE)

def replace_short_will(text):
   return re.sub(r" (.+)'ll", r' \1 will', text, flags=re.IGNORECASE)

def replace_short_would_had(text):
   # Note: short 'd could be would or had
   random_replacement = random.choice(['would', 'had'])
   return re.sub(r" (.+)'d", r' \1 ' + random_replacement, text, flags=re.IGNORECASE)   

def replace_short_to_be(text):
   text = re.sub("I'm", 'I am', text, flags=re.IGNORECASE)
   text = re.sub(r" (.+)'re", r' \1 are', text, flags=re.IGNORECASE)
   # 's cannot be replaced safe, as it could be expressing possesion 
   return text