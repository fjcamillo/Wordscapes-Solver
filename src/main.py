import json
import numpy as np
import argparse
import reader
import process
import pprint
import sys

def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument('letters', metavar='N', type=str, nargs='+', help='gather strings')
    args = parser.parse_args()

    question = np.array(args.letters)
    question_range = range(3, question.shape[0])

    for i in question_range:
        
        

        clean = process.clean(question)
        words = reader.read('../english-words/words_dictionary.json')

        print(len(words))

        if not words:
            print('Cannot Find Words')
            sys.exit(1)

        equivalent = process.words(words, clean)
        
        pprint.pprint([ d['words'] for d in equivalent])
    return



if __name__ == '__main__':
    main()