import json
import numpy as np
import constants
from typing import Dict

def read(name):
    try:
        with open(name, 'r') as f:
           words = json.load(f) 

        data = [ 
        {
            'numbers': np.array(
                [ 
                    int(constants.alphabet[letter.lower()]) if letter.lower() in constants.alphabet.keys() else 26 
                    for letter in word 
                ], dtype=int), 
            'word': word
        } for word in words ] # type: Dict[int, str]

    except:
        return
    return data