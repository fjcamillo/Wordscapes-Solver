import json
import numpy as np
import argparse
import reader
import process
import pprint
import sys
from itertools import combinations

def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument('letters', metavar='N', type=str, nargs='+', help='gather strings')
    args = parser.parse_args()

    question = np.array(args.letters)
    question_range = range(3, question.shape[0]+1)
    words = reader.read('../english-words/words_dictionary.json')
    if not words:
        print('Cannot Find Words')
        sys.exit(1)
    answers = []

    for i in question_range:
        
        combination = combinations(question, i)

        for combi in combination:
            clean = process.clean(combi)
            equivalents = process.words(words, clean)
            for equivalent in equivalents:
                answers.append(equivalent['words'])
    
    pprint.pprint(answers)

    return



if __name__ == '__main__':
    main()