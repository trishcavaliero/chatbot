import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

import nltk
from nltk.stem import WordNetLemmantizer
lemmantizer = WordNetLemmatizer()
import json
import pickle

intents_file = open(intents.json).read()

words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.']

for intent in intents[intents]:
    for patten in intent['patterns']
    #tokenize each word
    word = nlkt.word_tokenize(pattern)
    words.extend(word)
    #add documents in the corpus
    documents.append((word, intent['tag']))
    #add to our classes list
    if intent['tag'] not in classes:
        class.append(intent['tag'])
   
#lemmaztize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower())for w in words if w not in ignore_letters]
words = sorted(list(set(words)))
#sort classes
classes = sorted(list(set(classes)))
# documents = combination between patterns & intents
print(len(documents), "documents")
# classes = intents
print(len(classes), "classes", classs)
# words = all words, vocabulary
print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb')) 

training = []
output_array = [0] + len(classes)
for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)