from nltk.corpus import wordnet

stop_suffixes = set(['for', 'on', 'as', 'to', 'upon', 'into', 'by', 'at',
                     'against', 'with'])
whitelist = set(['carry on', 'come to', 'drone on', 'get it on', 'go on',
                 'hang on', 'hold on', 'know what\'s going on', 'latch on',
                 'live on', 'log on', 'look on', 'march on', 'move on',
                 'pass on', 'press on', 'push on', 'ramble on', 'rattle on',
                 'sign on'])
blacklist = set(['abound in', 'allow in', 'ask in', 'beat in', 'believe in',
                 'box in', 'brick in', 'bring in', 'build in', 'cage in',
                 'chisel in', 'clue in', 'color in', 'colour in',
                 'contract in', 'do in', 'drag in', 'draw in', 'drill in',
                 'feed in', 'fence in', 'file in', 'fill in', 'frame in',
                 'gather in', 'glass in', 'hammer in', 'hold in', 'inhere in',
                 'keep in', 'let in', 'lock in', 'lodge in', 'mix in',
                 'muster in', 'originate in', 'out in', 'partake in',
                 'persist in', 'phase in', 'pipe in', 'put in', 'rail in',
                 'rake in', 'range in', 'rein in', 'rope in', 'rough in',
                 'rule in', 'seal in', 'send in', 'shut in', 'sow in',
                 'stave in', 'stick in', 'take in', 'teem in', 'tie in',
                 'toss in', 'trade in', 'usher in', 'vote in', 'wall in',
                 'work in'])

def word_allowed(word):
    if word in whitelist:
        return True
    if word in blacklist:
        return False
    toks = word.split()
    return len(toks) == 1 or toks[-1] not in stop_suffixes

with open('verbs.txt', 'w') as ofile:
    words = set(lemma.name().replace('_', ' ')
                for synset in wordnet.all_synsets(wordnet.VERB)
                for lemma in synset.lemmas())
    for word in sorted(words):
        if word_allowed(word):
            ofile.write(word)
            ofile.write('\n')
