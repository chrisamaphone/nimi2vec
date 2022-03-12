# Train models using gensim
import gensim, logging, os
from gensim.models import Word2Vec
from gensim.test.utils import datapath
from preproc import preprocess
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# corpus_name = 'mdm-plus-pu';
corpus_name = 'all';

### n.b.: replaced this with preprocess fn in preproc to split out
####  punctuation
# sentences = []
# def read_input(path):
#     with open(path) as f:
#         for line in f:
#             # sentence = gensim.utils.simple_preprocess(line)
#             sentence = line.split()
#             sentences.append(sentence)

sentences = preprocess(corpus_name);

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
