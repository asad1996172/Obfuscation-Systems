import re
from Evaluation import POSTagging as pt


def replace_numbers(text):
    pos_tagged = pt.pos_tag(text)
    result = []
    for tagged_word in pos_tagged:
        if tagged_word[1] == 'NUM':
            num_to_string = nums_to_words(tagged_word[0])
            result.append((num_to_string, 'NUM'))
        else:
            result.append(tagged_word)
    return pt.pos_tagged_sentence_to_string(result)

'''
Given a CD from POS Tagging,
split it into number strings and then convert them to words.

If a number contains more than 8 numbers, then spell it digit by digit.
(Ex.: it might be a phone number.)
'''
def nums_to_words(num_string):
    result = num_string
    nums = re.split('\D', num_string)
    for num in nums:
        if len(num) > 0:
            word = ''
            if len(num) >= 8:
                for d in num:
                    if len(word) > 0: 
                        word = word + '-'
                    word = word + num_to_words(int(d))
            else:
                word = num_to_words(int(num))
            result = result.replace(num, word)
    return result

'''
words = {} convert an integer number into words

Source: http://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
'''
def num_to_words(num, join=True):
    # if not any(i.isdigit() for i in num):
    #     print('!!!! no digits ' + num)
    #     return num
    # print ('continue ' + num)

    # num = int(num)
    
    units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen', \
             'Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy', \
            'Eighty','Ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('Zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = int((numStrLen+2)/3)
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = int(groups-(i/3+1))
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words
