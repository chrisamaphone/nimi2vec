# Train models using gensim
import gensim, logging, os
from gensim.models import Word2Vec
from gensim.test.utils import datapath
from preproc import read_input
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus_relpath = 'corpus/mdm-plus-pu.txt';
corpus_path = os.path.abspath(corpus_relpath);

### n.b.: replaced this with read_input fn in preproc to split out
####  punctuation
# sentences = []
# def read_input(path):
#     with open(path) as f:
#         for line in f:
#             # sentence = gensim.utils.simple_preprocess(line)
#             sentence = line.split()
#             sentences.append(sentence)

sentences = read_input(corpus_path);

logging.info('Done reading corpus file');

# model = gensim.models.Word2Vec(corpus_file=datapath(corpus_path), vector_size=100, epochs=6);
model = gensim.models.Word2Vec(
        sentences,
        vector_size=100,
        window=5,
        sg=1, # added: try skipgram model
        min_count=2)
        # , workers=10)
model.train(sentences, total_examples=len(sentences), epochs=6)

logging.info("Training complete, saving model")

model.wv.save_word2vec_format(os.path.abspath('models/w2v.txt'));
