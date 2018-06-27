import numpy as np
import constants

def words(words, question):
    
    if not question.any() or not words: return
    sorted_question = np.sort(question)
    
    equate = [ {'numbers':np.sort(d['numbers']), 'words': d['word']} for d in words ]

    filter_by_shape = [ eq for eq in equate if eq['numbers'].shape[0] == question.shape[0] ]

    answers = [ ans for ans in filter_by_shape if np.array_equal(ans['numbers'], sorted_question) ]

    return answers

def clean(question):
    """
    Converts question to numeric values
    """

    clean = np.array([ constants.alphabet[d] for d in question ])

    return clean