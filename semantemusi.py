import os
import gensim
import random

from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors, Word2Vec

# glove model
# model_path = os.path.abspath('models/glove-vectors.txt');

# w2v model
model_path = os.path.abspath('models/w2v.txt');

model_file = datapath(model_path);
model = KeyedVectors.load_word2vec_format(model_file, binary=False);

# switch to a different model file
# noheader should be False if using w2v format, true if using GloVe
def switch_model(mname='w2v', noheader=False):
    newpath = os.path.abspath('models/'+mname+'.txt');
    newfile = datapath(newpath);
    model = KeyedVectors.load_word2vec_format(newfile, binary=False,
            no_header=noheader);

# Game stuff

# Convert a value in the range (-1, 1)
# to a "percent similarity" (0-100 range)
def getPct(value):
    return (value + 1)/2 * 100;

def guess(guessed_word):
    return getPct(model.similarity(guessed_word, secret_word));

# Open wordlist
possible_words = []
lines = []
with open('wordlist.txt') as f:
    lines = f.readlines();

for line in lines:
    possible_words.append(line.strip());

secret_word = random.choice(possible_words)


