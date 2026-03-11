import re
from num2words import num2words

import pandas as pd

data = pd.read_csv("fake.csv")

data=data.head()

title = data['title']
texts = data['text']

def clean_text(text):
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', ' ', text)
    
    text = re.sub(r'\d+', ' ', text)
    
    symbols = ['@', '#', '$', '%', '&', '*']
    for sym in symbols:
        text = text.replace(sym, ' ')
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
clean_texts = []

for t in texts:
    clean_texts.append(clean_text(str(t)))
tokenized_texts = []

for text in clean_texts:
    tokens = text.split()
    tokenized_texts.append(tokens)


vocab = []

for doc in tokenized_texts:
    for word in doc:
        if word not in vocab:
            vocab.append(word)
            
def vectorize(doc, vocab):
    
    vector = []
    
    for word in vocab:
        if word in doc:
            vector.append(1)
        else:
            vector.append(0)
    
    return vector


vectors = []

for doc in tokenized_texts:
    vectors.append(vectorize(doc, vocab))
dataset = []

for i in range(len(vectors)):
    
    dataset.append((vectors[i], title[i]))
    
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()

model.fit(vectors, title)


