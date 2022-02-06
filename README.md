An implementation of "semantle" (see https://semantle.novalis.org/) for the Toki Pona conlang (see https://tokipona.org/).

Usage:

<code>$ python3
>>> exec(open('semante-musi.py').read())
>>> guess('your_guess')
</code>

Returns a number between 0-1 for similarity.


Corpus sources:
- "mdm" (Matthew Dean Martin) files:
https://github.com/matthewdeanmartin/tokipona.parser/tree/master/TokiPonaTools/TokiPona/corpus
- "pu": https://gist.github.com/increpare/10d94b6d7f223dd0f07c73b10dadc020

If you want to (re)train on these corpora or your own, you can use the (included) <code>train-models.py</code> file, or save your own trained models in the <code>models/</code> folder (in word2vec KeyedVectors format).
