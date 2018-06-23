import numpy as np
import constants

def words(words, question):
    
    if not question.any() or not words: return

    equate = [ d['numbers'].sort() for d in words ]

    filter_by_shape = [ eq for eq in equate if eq.shape[0] == question.shape[0] ]

    answers = [ ans for ans in filter_by_shape if ans == question ]

    return answers

def clean(question):

    clean = np.array([ constants.alphabet[d] for d in question ])

    return clean