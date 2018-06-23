import json
import numpy as np
import argparse

def read(name):
    data = 'Data Not Found'
    try:
        with open(name, 'w') as f:
           data = json.load(f) 
    except:
        print('Data wasnt Found')
    return data


def main():
    


    return



if __name__ == '__main__':
    main()