# -*- coding: utf-8 -*-
"""LFA_P1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BQgS27BqHoT52MB9E_lCsDyu5xTm0gbI
"""

# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATA SOURCES
# TO THE CORRECT LOCATION (/kaggle/input) IN YOUR NOTEBOOK,
# THEN FEEL FREE TO DELETE THIS CELL.
# NOTE: THIS NOTEBOOK ENVIRONMENT DIFFERS FROM KAGGLE'S PYTHON
# ENVIRONMENT SO THERE MAY BE MISSING LIBRARIES USED BY YOUR
# NOTEBOOK.

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'restaurant-reviews-for-nlp:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F3995919%2F6956832%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240422%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240422T165108Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3Db51ae429b141afb8f3b99562b45ba8f2a05ca37266df7ed8f17b80d926ec72ac32f4dae02db46df74ee893d72052fd899ebe595c7c77f63439591c4e43639f9c7bdda550812db29624a64c7c3468441f9ac50b092770edc89e54aa5021c5fbc920f24058e62b872ab20cc276839c88162933c3b31748f56b0ef6aca450299974d13af20625c4b80b53daf5a8bcc31a2dd64d5102ecbb8eb7c1bef88bca8f6d0c6e94929a74dc7f63a2c30ee5f96fb089b6901dbe71a9836e74eb668c555190921daa7c89209e36a147c8aba769723c12cc151b84cde5f97fed8429a811ca3a5b9329c4709287fd2766f11d52d8703ecfd863b104a339cf39b7ee765650f3da22'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')

"""# Natural Language Processing (NLP)

## Importando as bibliotecas
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importando o dataset"""

dataset = pd.read_csv('/kaggle/input/restaurant-reviews-for-nlp/Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

"""## Fazendo a limpeza no texto"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder

corpus = []
for i in range(0, 1000):
  review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  # all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

dataset

print(corpus)

"""## Crindo o modelo de agrupamento de palavras"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

"""## Separando o dataset em treino e teste"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""## Treinando o modelo Naive Bayes no dataset de treino"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

"""## Predizendo o resultado dos testes"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Matriz de confusão e métricas de avaliação"""

from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, jaccard_score

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Acurácia
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)

# F1-Score
f1 = f1_score(y_test, y_pred)
print("F1-Score:", f1)

# IoU (Jaccard Score)
iou = jaccard_score(y_test, y_pred)
print("IoU (Jaccard Score):", iou)

# pip install --upgrade scikit-learn

"""# Aplicando autômatos para encontrar palavras a partir das keywords"""

import re
from collections import defaultdict

class Automaton:
    def __init__(self):
        self.transitions = defaultdict(dict)
        self.accept_state = None

    def add_transition(self, src_state, dst_state, char):
        self.transitions[src_state][char] = dst_state

    def add_accept_state(self, state):
        self.accept_state = state

# Construção do autômato para uma palavra específica
def build_automaton(word):
    automaton = Automaton()
    prev_state = None
    for char in word:
        if prev_state is None:
            automaton.add_transition(0, 1, char)
            prev_state = 1
        else:
            prev_state += 1
            automaton.add_transition(prev_state - 1, prev_state, char)
    automaton.add_accept_state(prev_state)
    return automaton

# Pré-processamento e construção dos autômatos para cada palavra-chave
keywords = ['delicious', 'tasti', 'appetizing','fantast', 'great', 'tempting', 'exquisite', 'nutritious', 'comforting', 'love', 'fresh',
            'stimulating', 'irresistible', 'divine', 'great', 'best', 'satisfying', 'loved', 'exotic', 'heavenly', 'spoiled', 'tasteless',
            'worst', 'suck', 'bad', 'greasy', 'burn', 'hella', 'salti', 'tasteless', 'sour', 'horribl', 'stink', 'unpleasant', 'disappoint',
            'wait', 'nasty', 'not', 'meh', 'never']

automata = [build_automaton(keyword) for keyword in keywords]

def pattern_matching(sentence, automata):
    matches = []
    for word in sentence.lower().split():
        for automaton in automata:
            current_state = 0
            for char in word:
                if char in automaton.transitions[current_state]:
                    current_state = automaton.transitions[current_state][char]
                if current_state == automaton.accept_state:
                    matches.append(word)
                    break
    return matches

reviews = dataset['Review']  # Assuming reviews is a list of strings
matched_keywords = []
for review in reviews:
    review_matches = pattern_matching(review, automata)  # Directly pass the string
    if review_matches:
        print(f"Review:")  # No ID available for string reviews
        print(f"Keywords found: {review_matches}")
        print("--------------------------")
        matched_keywords.extend(review_matches)

# Print the overall list of matched keywords
print("Total matched keywords:", matched_keywords)

# Definir pesos para palavras positivas e negativas

palavras_positivas = {'delicious': 2, 'tasti':2, 'appetizing':1,'fantast':2, 'great':2, 'tempting':1, 'exquisite':2, 'nutritious':1, 'comforting':1, 'love':2,
                      'fresh':1, 'stimulating':1, 'irresistible':2, 'divine':2, 'best':1, 'colorful':1, 'crispy':1, 'satisfying':1, 'exotic':2, 'loved':2}
palavras_negativas = {'spoiled':-1, 'tasteless':-2, 'worst':-2, 'suck':-1, 'bad':-1, 'greasy':-2, 'burn':-2, 'hella':-1, 'salti':-2, 'sour':-2,
                      'horribl':-2, 'stink':-1, 'unpleasant':-1, 'disappoint':-1, 'wait':-2, 'nasty':-2, 'soggy':-1, 'not':-1, 'meh':-2, 'never':-1}

palavras_positivas['delicious']

# Avaliação das avaliações
def avaliar_avaliacoes():
    automato = Automato()
    for index, row in dataset.iterrows():
        review = dataset['Review']
        score = 0
        countp = 0
        countn = 0
        for review in reviews:
            for word in review.split():
                # print(word)
                # if palavras_positivas[word] != '':
                #   print(word)
                if word in palavras_positivas:
                    score += palavras_positivas[word]
                    countp +=1
                    # print(palavras_positivas[word])
                elif word in palavras_negativas:
                    score += palavras_negativas[word]
                    countn+=1
            if automato.recognize(review):
                score *= 2  # Ajuste para palavras reconhecidas

    # Atribuir classificação de estrelas com base na pontuação
    score = score/(countn+countp)
    print(score)
    if score == 2:
        print('O restaurante teve avaliação de 5 ★★★★★')
    elif score < 2 and score >= 1:
        print('O restaurante teve avaliação de 4 ★★★★☆')
    elif score <1 and score >=0:
        print('O restaurante teve avaliação de 3 ★★★☆☆')
    elif score <0 and score >=-1:
        print('O restaurante teve avaliação de 2 ★★☆☆☆')
    else:
        print('O restaurante teve avaliação de 1 ★☆☆☆☆')
    return dataset

# Avaliar as avaliações e apresentar os resultados
dataset = avaliar_avaliacoes()
# print(dataset[['classificacao']])

"""##ERROR"""

def avaliar_avaliacoes(dataset):
    automato = Automato()

    # Initialize empty lists to store scores and classifications
    scores = []
    classifications = []

    for index, row in dataset.iterrows():
        review = dataset.loc[index, 'Review']
        review_score = 0

        # Calculate score for each review
        for word in review.split():
            if word in palavras_positivas:
                review_score += palavras_positivas[word]
            elif word in palavras_negativas:
                review_score += palavras_negativas[word]

        # Apply automaton multiplier if recognized
        if automato.recognize(review):
            review_score *= 2

        # Append review score and classification based on score
        scores.append(review_score)
        if review_score > 2:
            classifications.append('★★★★★')
        elif review_score > 0:
            classifications.append('★★★★☆')
        elif review_score == 0:
            classifications.append('★★★☆☆')
        elif review_score >= -2:
            classifications.append('★★☆☆☆')
        else:
            classifications.append('★☆☆☆☆')

    # Calculate average score
    average_score = sum(scores) / len(scores)

    # Assign overall classification based on average score
    overall_classification = None
    if average_score > 2:
        overall_classification = '★★★★★'
    elif average_score > 0:
        overall_classification = '★★★★☆'
    elif average_score == 0:
        overall_classification = '★★★☆☆'
    elif average_score >= -2:
        overall_classification = '★★☆☆☆'
    else:
        overall_classification = '★☆☆☆☆'

    # Update dataset with classifications and overall classification
    dataset['classificacao'] = classifications
    dataset['classificacao_geral'] = overall_classification

    return dataset

# Avaliar as avaliações e apresentar os resultados
dataset = avaliar_avaliacoes(dataset)
print(dataset[['Review', 'classificacao', 'classificacao_geral']])

# Reconhecimento de padrões
def pattern_matching(sentence):
    matches = []
    for word in sentence.split():
        print(word)
        for automaton in automata:
            current_state = 0
            for char in word:
                if char in automaton.transitions[current_state]:
                    current_state = automaton.transitions[current_state][char]
            if current_state == automaton.accept_state:
                matches.append(word)
    return matches

review = dataset['Review'][1]
matches = pattern_matching(review.lower())
if matches:
    print("Palavras-chave encontradas:", matches)
else:
    print("Nenhuma palavra-chave encontrada na avaliação.")

def pattern_matching(sentence, automata):
    matches = []
    for word in sentence.lower().split():
        for automaton in automata:
            current_state = 0
            for char in word:
                if char in automaton.transitions[current_state]:
                    current_state = automaton.transitions[current_state][char]
                if current_state == automaton.accept_state:
                    matches.append(word)
                    break
    return matches

# Assuming 'reviews' is a list of review objects with a 'sentence' attribute
# and 'automata' is a list of automata representing keyword patterns
reviews = dataset['Review']
matched_keywords = []
for review in reviews:
    review_matches = pattern_matching(review.sentence, automata)
    if review_matches:
        print(f"Review ID: {review.id}")
        print(f"Keywords found: {review_matches}")
        print("--------------------------")
        matched_keywords.extend(review_matches)

# Print the overall list of matched keywords
print("Total matched keywords:", matched_keywords)