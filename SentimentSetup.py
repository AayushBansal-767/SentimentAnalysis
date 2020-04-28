import nltk
import random
import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

documents_f = open("pickle/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()


word_features_f = open("pickle/word_features.pickle", "rb")
word_features = pickle.load(word_features_f)
word_features_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

featuresets_f = open("pickle/featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)

testing_set = featuresets[10000:]
training_set = featuresets[:10000]



open_file = open("pickle/naivebayes.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()


def sentiment(text):
	feats=find_features(text)
	return classifier.classify(feats)