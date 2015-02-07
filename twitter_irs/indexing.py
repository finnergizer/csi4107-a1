from collections import Counter
from twitter_irs.preprocessor import pre_process, parse_corpus
from twitter_irs.utils import process_txt
import json

__author__ = 'shaughnfinnerty'


def corpus_counter(corpus):
    corpus_counter = []
    for doc in corpus:
        corpus_counter.append({"id": doc["id"], "msg_counter": Counter(doc["msg"])})
    return corpus_counter

def indexing(corpus_counter, tokens):
    """ Creates an inverted index with hashes using message id as key and frequency as value"""
    inverted_index = {}
    i=1
    for token in tokens:
        inverted_index[token] = {}
        if (i % 1000 == 0):
            print(str(float(i)/len(tokens)*100) + "% Complete")
            with open("index/index-output"+str(i)+".txt", "w") as f:
                f.write(json.dumps(inverted_index))
        i=i+1
        for document in corpus_counter:
            # msg_tokens = process_txt(document["msg"])
            counter = document["msg_counter"]
            freq = counter[token]
            if freq > 0:
                # inverted_index[token].append({"id": document["id"], "freq": freq})
                inverted_index[token].update({document["id"]: freq})

    return inverted_index


def indexToFile(index):
    """ Outputs the inverted index to a text file, tab-separated.  Not very readable."""
    with open("index-output-new.txt", "wb") as f:
        f.write(json.dumps(index))

def loadIndex(path):
    index = {}
    with open(path, "rb") as f:
        index = json.loads(f.read())
    return index;
#

# #Creating the index... Will need to package this more gracefully in a function
# corpus = parse_corpus();
# print "parsed corpus"
# print len(corpus)
# tokens = pre_process(corpus);
# print "tokens created";
#
# corpus_counter = corpus_counter(corpus);
# print "created corpus_counter" + str(len(corpus_counter))
# index = indexing(corpus_counter, tokens);
# print "index created"
# indexToFile(index)
# print "index saved"

