import os
import gensim
import random

from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors, Word2Vec

path_glove = os.path.abspath('models/glove-vectors.txt');
glove_file = datapath(path_glove);

model = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True);

# Convert a value in the range (-1, 1)
# to a "percent similarity" (0-100 range)
def getPct(value):
    return (value + 1)/2 * 100;

def guess(guessed_word):
    return getPct(model.similarity(guessed_word, secret_word));

# switch to a different model file
# noheader should be False if using w2v format, true if using GloVe
def switch_model(mname='w2v', noheader=False):
    newpath = os.path.abspath('models/'+mname+'.txt');
    newfile = datapath(newpath);
    model = KeyedVectors.load_word2vec_format(newfile, binary=False,
            no_header=noheader);

switch_model(); # Switch to w2v instead of glove

# Game stuff

possible_words = []
lines = []
with open('wordlist.txt') as f:
    lines = f.readlines();

for line in lines:
    possible_words.append(line.strip());

secret_word = random.choice(possible_words)


