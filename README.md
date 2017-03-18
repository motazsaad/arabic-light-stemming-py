# Arabic Light Stemming Python 
Arabic Light stemming with Python 

This code performs light stemming for Arabic words. The implementation is based on ISRI Arabic Stemmer, which is a rooting algorithm for Arabic text. ISRI Arabic Stemmer is described in:

Taghva, K., Elkoury, R., and Coombs, J. 2005. Arabic Stemming without a root dictionary. Information Science Research Institute. University of Nevada, Las Vegas, USA.

## Arabic Light Stemming Steps

1. remove diacritics which representing Arabic short vowels 
2. remove length three and length two prefixes in this order
3. remove length three and length two suffixes in this order
4. remove connective ‘و’ if it precedes a word beginning with ‘و’
5. normalize initial hamza to bare alif

For more information, please refer to http://www.nltk.org/_modules/nltk/stem/isri.html

Please note steps are derived from http://www.nltk.org/_modules/nltk/stem/isri.html#ISRIStemmer.stem

## Install requirements 
```pip install -r requirements```