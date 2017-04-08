import argparse

from nltk.stem.isri import ISRIStemmer
import sys


# Arabic light stemming for Arabic text
# takes a word list and perform light stemming for each Arabic words
def light_stem(text):
    words = text.split()
    result = list()
    stemmer = ISRIStemmer()
    for word in words:
        word = stemmer.norm(word, num=1)      # remove diacritics which representing Arabic short vowels
        if not word in stemmer.stop_words:    # exclude stop words from being processed
            word = stemmer.pre32(word)        # remove length three and length two prefixes in this order
            word = stemmer.suf32(word)        # remove length three and length two suffixes in this order
            word = stemmer.waw(word)          # remove connective ‘و’ if it precedes a word beginning with ‘و’
            word = stemmer.norm(word, num=2)  # normalize initial hamza to bare alif
        result.append(word)
    return ' '.join(result)

parser = argparse.ArgumentParser(description='performs light stemming for Arabic words.')

parser.add_argument('-i', '--infile', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file.', required=True)
parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', encoding='utf-8'),
                    help='out file.', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    lines = args.infile.readlines()
    for line in lines:
        text = light_stem(line)
        args.outfile.write(text + "\n")
