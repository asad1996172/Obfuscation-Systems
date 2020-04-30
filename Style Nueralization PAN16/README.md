## Style Nuetralization PAN16

#### This code repo is from (https://bitbucket.org/pan2016authorobfuscation/authorobfuscation/src/master/)
========================================================================

This is the code initially used for the Author Obfuscation task in PAN-2016 
competition[1].
The system [2] calculates average measures of different features for author 
identification and applies transformation to a given text so that its metrics are 
adjusted towards the average calculated level.


---
-1- CONTENTS
---


  * README.txt   
    this file	
	
  * AuthorObfuscation/AuthorObfuscation/AuthorObfuscation  
	contains the code for text obfuscation 
	
  * AuthorObfuscation/AuthorObfuscation/AuthorObfuscation/Dictionaries  
	contains the vocabularies used for the different transformations
  

---
-2- ABSTRACT
---

Users posting online expect to remain anonymous unless they have logged in, which is often needed for
them to be able to discuss freely on various topics. Preserving the anonymity of a text's writer can be also
important in some other contexts, e.g., in the case of witness protection or anonymity programs. However,
each person has his/her own style of writing, which can be analyzed using stylometry, and as a result, the
true identity of the author of a piece of text can be revealed even if s/he has tried to hide it. Thus, it could
be helpful to design automatic tools that can help a person obfuscate his/her identity when writing text. In
particular, here we propose an approach that changes the text, so that it is pushed towards average values
for some general stylometric characteristics, thus making the use of these characteristics less
discriminative. The approach consists of three main steps: first, we calculate the values for some popular
stylometric metrics that can indicate authorship; then we apply various transformations to the text, so that
these metrics are adjusted towards the average level, while preserving the semantics and the soundness of
the text; and finally, we add random noise. This approach turned out to be very efficient, and yielded the
best performance on the Author Obfuscation task at the PAN-2016 competition.

  
---    
-3- LICENSING
---

Usage of this code is free for general research use.

  
---
-4- CITATION
---

You should use the following citation in your publications when using this code 
and resources:

@InProceedings{karadzhov-EtAl:2017:clef2017,
  author    = {Karadzhov, Georgi and
			Mihaylova, Tsvetomila and
			Kiprov, Yasen and
			Georgiev, Georgi and
			Koychev, Ivan and
			Nakov, Preslav},
  title     = {The Case for Being Average: A Mediocrity Approach to 
				Style Masking and Author Obfuscation},
  booktitle = {Experimental IR Meets Multilinguality, Multimodality, 
				and Interaction},
  year      = {2017},
  chapter   = {18},
  doi		= {10.1007/978-3-319-65813-1_18}
}




---
-5- CREDITS
---

Georgi Karadzhov, Sofia University "St. Kliment Ohridski", Bulgaria, georgi.m.karadjov@gmail.com
Tsvetomila Mihaylova, Sofia University "St. Kliment Ohridski", Bulgaria, tsvetomila.mihaylova@gmail.com
Yasen Kiprov, Sofia University "St. Kliment Ohridski", Bulgaria, yasen.kiprov@gmail.com
Georgi Georgiev, Sofia University "St. Kliment Ohridski", Bulgaria, g.d.georgiev@gmail.com
Ivan Koychev, Sofia University "St. Kliment Ohridski", Bulgaria, koychev@fmi.uni-sofia.bg
Preslav Nakov, Qatar Computing Research Institute, HBKU, Qatar, pnakov@hbku.edu.qa

Acknowledgments:
This research was performed by a team of students from MSc programs in Computer
Science in the Sofia University "St. Kliment Ohridski". The work is supported 
by the NSF of Bulgaria under Grant No.: DN 02/11/2016 - ITDGate.


---
-6- REFERENCES
---

1. Potthast, M., Hagen, M., Stein, B.: Author obfuscation: Attacking the state of the art in
authorship verification. In: Working Notes of CLEF 2016 - Conference and Labs of the
Evaluation Forum. pp. 716-749. CLEF '16, Evora, Portugal (2016)
2. Mihaylova, T., Karadjov, G., Nakov, P., Kiprov, Y., Georgiev, G., Koychev, I.:
SU@PAN'2016: Author Obfuscation-notebook for PAN at CLEF 2016. In: Working
Notes of CLEF 2016 - Conference and Labs of the Evaluation Forum (CLEF 2016),
Evora (2016)
