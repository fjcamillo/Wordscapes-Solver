import numpy as np
import constants

def words(words, question):
    
    if not question.any() or not words: return
    sorted_question = np.sort(question)
    
    equate = [ {'numbers':np.sort(d['numbers']), 'words': d} for d in words ]

    filter_by_shape = [ eq for eq in equate if eq['numbers'].shape[0] == question.shape[0] ]

    print(len(filter_by_shape))
    print(filter_by_shape[0:15])
    print(question)
    print(question.shape)

    answers = [ ans for ans in filter_by_shape if np.array_equal(ans['numbers'], sorted_question) ]

    return answers

def clean(question):

    clean = np.array([ constants.alphabet[d] for d in question ])

    return clean