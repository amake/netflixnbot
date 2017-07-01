from __future__ import print_function
import os
import sys
import random

verbs = []

def load_words(filename):
    if os.path.isfile(filename):
        with open(filename) as f:
            return f.read().splitlines()
    else:
        print(filename + ' not found. Generate it.')
        sys.exit(1)

verbs = load_words('verbs.txt')

def random_activity():
    return 'Netflix and %s' % random.choice(verbs)

if __name__ == '__main__':
    for _ in xrange(10):
        print(random_activity())
