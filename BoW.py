from sklearn.feature_extraction.text import CountVectorizer
import umap
import numpy as np
import plotly.express as px
import pandas as pd
import warnings
import random


def calculate_jaccard_dist(u, v):
    intersection = 0
    union = 0
    for i in range(len(u)):
        
        # The word is present in both vectors
        if u[i] > 0 and v[i] > 0:
            intersection += 1
            
        # The word is present in one of the vectors
        if u[i] > 0 or v[i] > 0:
            union += 1
            
    jaccard_dist = 1 - (intersection / union)
    return jaccard_dist

    
def get_bow_and_vocab(sentences):
    cv = CountVectorizer()
    bow = cv.fit_transform(sentences).toarray()
    vocab = cv.get_feature_names()
    print(bow,vocab)
    return bow, vocab

bow, vocab = get_bow_and_vocab(sentences)
print(list(zip(vocab, bow[0])))



