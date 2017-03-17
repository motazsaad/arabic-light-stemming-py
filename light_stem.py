from nltk.stem.isri import ISRIStemmer
import sys


# Arabic light stemming for Arabic text
# takes a word list and perform light stemming for each Arabic words
def light_stem(text):
    words = text.split()
    result = list()
    stemmer = ISRIStemmer()
    for word in words:
        word = stemmer.norm(word, num=1)      #  remove diacritics which representing Arabic short vowels
        if not word in stemmer.stop_words:    # exclude stop words from being processed
            word = stemmer.pre32(word)        # remove length three and length two prefixes in this order
            word = stemmer.suf32(word)        # remove length three and length two suffixes in this order
            word = stemmer.waw(word)          # remove connective ‘و’ if it precedes a word beginning with ‘و’
            word = stemmer.norm(word, num=2)  # normalize initial hamza to bare alif
        result.append(word)
    return ' '.join(result)


def usage():
    return "usage: python ", sys.argv[0] + "  <input file>  <output file>"

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        with open(input_file, encoding="utf-8") as file_reader, open(output_file, encoding="utf-8", mode='w') as file_writer:
            lines = file_reader.readlines()
            for line in lines:
                text = light_stem(line)
                file_writer.write(text + "\n")
    else:
        print(usage())