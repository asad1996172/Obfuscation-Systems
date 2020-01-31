This is the system used for PAN 2016, task Author Masking.

-------------------------------------------

Install:

1. install nltk, enum34, mstranslator
2. run download_nltk.py to download the necessary resources
3. Download corpus:
cd myapp/
mkdir nltk_data
python -m nltk.downloader
This'll pop up the nltk downloader. Set your Download Directory to absolute_path_to_myapp/nltk_data/

Need to download the following:
Corpora:
-> stopwords
-> wordnet
Models:
-> advanced_perceptron_tagger
-> punkt
-> universal_tagset

-------------------------------------------

Run:

python AuthorObfuscation.py -i input_dir -o output_dir

-------------------------------------------

Calculate corpus stats:

-> For caluclation of the average corpus values:

python corpus_stats.py -i input_dir


-> For comparison of values of files in a directory:

python corpus_stats.py -i input_dir -s dir

(-s dir means that the selected option is 'compare files in dir')



-------------------------------------------

Calced stats:

Metric                  | Average for train corpus | In file Big.txt    
--------------------------------------------------------------------
average_sentence_length | 18.417844096038532       | 19.35502733
sentence_count          | 54.05853658536585        | 57635
word_count              | 965.770731707317         | 1115527
unique_words_count      | 404.4390243902439        | 38157
unique_words_ratio      | 0.44343308546648763      | 0.034205358
misspelled_words_rate   | 0.3614716405460263       | 0.023366534
average_noun_rate       | 0.23241378845274205      | 0.258504725
average_verb_rate       | 0.2016751628812592       | 0.181682738
average_adj_rate        | 0.07680662114342511      | 0.076043879
average_adv_rate        | 0.07240434147752657      | 0.054954295
average_punct_rate      | 0.1375059959791054       | 0.160501718
stop_words_count        | 485.4829268292683        | 548492
stop_words_ratio        | 0.5156231373672724       | 0.491688682
all_capital_letters     | 0.027442878131310067     | 0.012777817
first_capital_letter    | 0.12645193748880598      | 0.108523594

-----------------------------------------------------