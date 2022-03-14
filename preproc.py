# preprocess a corpus file as follows:
# join lines until you hit a terminal marker [. ? ! " ']
# insert newline after each terminal marker
# remove all punctuation [. ? ! " ' , ; : -]

import os, re

terminal = ['.', '?', '!', '"', '\'']
terminal_re = '|'.join(terminal);
punct = [',', ';', ':', '-']
punct.extend(terminal)
punct_re = '|'.join(punct);

def process_line(line, start):
    sentences_from_line = []
    current_sentence = start
    tokens = re.findall(r"[\w']+|[.,!?;:]", line);
    for t in tokens:
        # current_sentence.append(t);
        if (t in terminal and len(current_sentence) > 0):
            sentences_from_line.append(current_sentence.copy())
            current_sentence = []
        elif (t in punct): # ignore punctuation
           continue
        else:
            current_sentence.append(t)
    # if the sentence doesn't end in a terminal, include it anyway
    # if len(current_sentence) > 0:
    sentences_from_line.append(current_sentence.copy())
    return sentences_from_line

outpath_rel = 'tmp/processed.txt';
outpath = os.path.abspath(outpath_rel);

def preprocess(fname_in):
    inpath_rel = 'corpus/'+fname_in+'.txt';
    inpath = os.path.abspath(inpath_rel);


    sentences = []
    remainder = []
    with open(outpath, "w") as outfile:
        with open(inpath) as infile:
            for line in infile:
                processed = process_line(line, remainder);
                end = len(processed)-1;
                remainder = processed[end];
                new_sentences = processed[0:end];
                sentences.extend(new_sentences);
                for sentence in new_sentences:
                    sent_string = " ".join(sentence)+"\n";
                    outfile.write(sent_string);
    return sentences


input_filename = "pu"


# read_input(inpath);
