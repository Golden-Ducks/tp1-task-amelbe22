# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

import numpy as np
from sklearn.cluster import KMeans

# Your Task: Fill these functions


import re

def preprocess_text(text):
    """
    Lowercase, remove punctuation, tokenize
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  
    tokens = text.split()
    return tokens
from collections import Counter

def vectorize(docs, n_gram_size=1):

    processed_docs = [preprocess_text(doc) for doc in docs]

    def create_ngrams(tokens, n):
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

    docs_ngrams = [create_ngrams(tokens, n_gram_size) for tokens in processed_docs]

    # build vocabulary
    vocab = sorted(set(ng for doc in docs_ngrams for ng in doc))
    vocab_index = {word:i for i,word in enumerate(vocab)}

    # build document vectors
    X = np.zeros((len(docs), len(vocab)))

    for doc_id, doc in enumerate(docs_ngrams):
        counts = Counter(doc)
        for word, count in counts.items():
            X[doc_id][vocab_index[word]] = count

    return X

# Training / Clustering

all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# 1-gram Experiment
X1 = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(X1)

# 2-gram Experiment
X2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(X2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")

# compare accuracy and precision

