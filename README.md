## nimi2vec, aka semantemusi

An implementation of "semantle" (see https://semantle.novalis.org/) for the Toki Pona conlang (see https://tokipona.org/).

Usage:

    $ python3
    >>> exec(open('semante-musi.py').read())
    >>> guess('your_guess')

Returns a number between 0-1 for similarity.
The target word is stored in a variable <code>secret_word</code>, so you can cheat and look at it, or poke around with other model queries, like <code>model.most_similar(secret_word)</code>.


Corpus sources:
- "mdm" (Matthew Dean Martin) files:
https://github.com/matthewdeanmartin/tokipona.parser/tree/master/TokiPonaTools/TokiPona/corpus
- "pu": https://gist.github.com/increpare/10d94b6d7f223dd0f07c73b10dadc020

If you want to (re)train on these corpora or your own, you can use the (included) <code>train-models.py</code> file, or save your own trained models in the <code>models/</code> folder (in word2vec KeyedVectors format).
