import sys
import pyfreeling
import sys

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
def ProcessSentences(ls):
    output = []
    # for each sentence in list
    for s in ls :
        # for each word in sentence
        for w in s :
            # print word form
            # print("word '"+w.get_form()+"'")
            # print possible analysis in word, output lemma and tag
            # print("  Possible Synsets: {"+w.get_senses_string()+"}")

            # print  best sense and its page rank value.
            rank = w.get_senses()
            selected_synset = None
            if len(rank)>0 :
                #  print analysis selected by the tagger
                # print("  Selected Synset: ("+rank[0][0]+","+str(rank[0][1])+")")
                selected_synset = rank[0][0]
            output.append((w.get_form(), selected_synset))
        # sentence separator
        print("")
    return output


## -----------------------------------------------
## Set desired options for morphological analyzer
## -----------------------------------------------
def my_maco_options(lang,lpath) :

    # create options holder
    opt = pyfreeling.maco_options(lang);

    # Provide files for morphological submodules. Note that it is not
    # necessary to set file for modules that will not be used.
    opt.UserMapFile = "";
    opt.LocutionsFile = lpath + "locucions.dat";
    opt.AffixFile = lpath + "afixos.dat";
    opt.ProbabilityFile = lpath + "probabilitats.dat";
    opt.DictionaryFile = lpath + "dicc.src";
    opt.NPdataFile = lpath + "np.dat";
    opt.PunctuationFile = lpath + "../common/punct.dat";
    return opt;



## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

# set locale to an UTF8 compatible locale
pyfreeling.util_init_locale("default");

# get requested language from arg1, or English if not provided
lang = "en"
if len(sys.argv)>1 : lang=sys.argv[1]

# get installation path to use from arg2, or use /usr/local if not provided
ipath = "/usr/local";
if len(sys.argv)>2 : ipath=sys.argv[2]

# path to language data
lpath = ipath + "/share/freeling/" + lang + "/"

# create analyzers
tk=pyfreeling.tokenizer(lpath+"tokenizer.dat");
sp=pyfreeling.splitter(lpath+"splitter.dat");

# create the analyzer with the required set of maco_options
morfo=pyfreeling.maco(my_maco_options(lang,lpath));
#  then, (de)activate required modules
morfo.set_active_options (False,  # UserMap
                          True,  # NumbersDetection,
                          True,  # PunctuationDetection,
                          True,  # DatesDetection,
                          True,  # DictionarySearch,
                          True,  # AffixAnalysis,
                          False, # CompoundAnalysis,
                          True,  # RetokContractions,
                          True,  # MultiwordsDetection,
                          True,  # NERecognition,
                          False, # QuantitiesDetection,
                          True); # ProbabilityAssignment

# create tagger
tagger = pyfreeling.hmm_tagger(lpath+"tagger.dat",True,2)

# create sense annotator
sen = pyfreeling.senses(lpath+"senses.dat");
# create sense disambiguator
wsd = pyfreeling.ukb(lpath+"ukb.dat");

def process_text(text):
    # process input text
    # tokenize input line into a list of words
    lw = tk.tokenize(text)
    # split list of words in sentences, return list of sentences
    ls = sp.split(lw)

    # perform morphosyntactic analysis and disambiguation
    ls = morfo.analyze(ls)
    ls = tagger.analyze(ls)
    # annotate and disambiguate senses
    ls = sen.analyze(ls);
    ls = wsd.analyze(ls);

    # do whatever is needed with processed sentences
    output = ProcessSentences(ls)
    return output