# -*- coding: utf-8 -*-
"""Movie-Review.ipynb

"""

import pandas as pd
import numpy as np
import io
from google.colab import files

upload = files.upload()

df  = pd.read_csv(io.BytesIO(upload['moviereviews2.tsv']),sep='\t')

df.head()

df.isnull().sum()

list = []

for ind, label, review in df.itertuples():
  if type(review) == str:
    if review.isspace():
      list.append(ind)

print(list)

len(list)

df.dropna(inplace=True)

df['label'].value_counts()

from sklearn.model_selection import train_test_split

X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X,  y, test_size=0.33, random_state = 42)

''' Building the pipeline '''

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf',TfidfVectorizer()),
                     ('clf',LinearSVC())])


text_clf.fit(X_train, y_train)

''' Prediction of X_test '''
prediction = text_clf.predict(X_test)

''' Confusion Matrix '''

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


print('The Confusion Matrix is \n{}'.format(confusion_matrix(y_test, prediction)),'\n\n\n')
print('The Classification Report is \n {}'.format(classification_report(y_test,prediction)),'\n\n\n')
print('The Accuracy is \n {}'.format(accuracy_score(y_test,prediction)),'\n\n\n')

''' Prediction of the input '''

text_clf.predict(['i liked this one'])

text_clf.predict(['i did not liked this movie'])
