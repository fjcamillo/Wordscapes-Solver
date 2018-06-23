import json
import numpy as np
import argparse
import reader
import process
import pprint
import sys

def main():
    

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-letters')
    question = np.array([ 'p', 'a', 'r', 'k'])
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