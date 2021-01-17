import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

dataset=pd.read_csv('prod_tasklist.csv', encoding='cp1252')

sentences=dataset['TASK'].to_list()

vocab_size = 5908
embedding_dim = 16
max_length = 10
trunc_type='post'
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words = vocab_size, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, maxlen=max_length, truncating=trunc_type)


nei_clf = NearestNeighbors(p=2,metric='cosine')
nei_clf.fit(padded)

i=sentences.index('Alert for new database creation')

distances,indices = nei_clf.kneighbors(np.expand_dims(padded[i],axis=0),n_neighbors=10)
index_list=indices.flatten().tolist()
res_list = [sentences[i] for i in index_list] 
print('query search :',sentences[i])
print('recommended scripts',list(set(res_list))[:5])
