from Evaluation import POSTagging as pt

def obfuscate_all_uppercase_words(text):
    pos_tagged = pt.pos_tag(text)
    result = []
    for n,tagged_word in enumerate(pos_tagged):
        # Capitalize only the words longer than 3 symbols, the rest could be abbreviations
        if tagged_word[0].isupper() and len(tagged_word[0]) > 3:
            result.append((tagged_word[0].capitalize(), tagged_word[1]))
        else:
            result.append(tagged_word)
    return pt.pos_tagged_sentence_to_string(result)