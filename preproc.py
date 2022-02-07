# preprocess a corpus file as follows:
# join lines until you hit a terminal marker [. ? ! " ']
# insert newline after each terminal marker
# remove all punctuation [. ? ! " ' , ; : -]

import os, re

inpath_rel = 'corpus/pu.txt';
inpath = os.path.abspath(inpath_rel);

outpath_rel = 'tmp/pu-processed.txt';
outpath = os.path.abspath(outpath_rel);

terminal = ['.', '?', '!', '"', '\'']
terminal_re = '|'.join(terminal);
punct = [',', ';', ':', '-']
punct.extend(terminal)
punct_re = '|'.join(punct);

def process_line(line):
    sentences_from_line = []
    current_sentence = []
    tokens = re.findall(r"[\w']+|[.,!?;]", line);
    for t in tokens:
        if (t in terminal and len(current_sentence) > 0):
            sentences_from_line.append(current_sentence.copy())
            current_sentence = []
        elif (t in punct):
            continue
        else:
            current_sentence.append(t)
    # if the sentence doesn't end in a terminal, include it anyway
    if len(current_sentence) > 0:
        sentences_from_line.append(current_sentence.copy())
    return sentences_from_line

def read_input(path):
    sentences = []
    with open(path) as f:
        for line in f:
            sentences.extend(process_line(line));
    return sentences

# read_input(inpath);
