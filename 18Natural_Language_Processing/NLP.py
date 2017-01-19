#Natural Language Processing

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def F1_Score(cm):
    
    """ Used to calculate performace of the classification method"""

    accuracy = (float(cm[0,1]) + cm[1,0])/(float(cm[0,0]) + cm[1,1]+ cm[0,1] + cm[1,0])
    precision = round(float(cm[0,0])/(cm[0,0]+cm[0,1]),4)
    recall = round(float(cm[0,0])/(cm[0,0]+cm[1,0]),4)
    F1 = round(2 * precision * recall / (precision + recall),2)
    
    print ("------------------------------------------------------")
    print (method + "\n")
    print ("Accuracy - " + str(accuracy))
    print ("Precision - " + str(precision))
    print ("Recall - " + str(recall))
    print ("------------------------------------------------------")
    print ("F1 Score - " + str(F1))
    print ("------------------------------------------------------\n")


#Importing data
dataset = pd.read_csv("Restaurant_Reviews.tsv",delimiter = "\t", quoting = 3)
#quoting = 3 for ignoring double quotes in the dataset

#Cleaning the text
import re

#Importing a list of useless words
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(len(dataset)):
    #Removed punctuations and non-letters (only kept letters)
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])

    #Everything lower cases
    review = review.lower()
    
    #Split the review into a list
    review = review.split()
    
    #Remove 'stopwords' from the sentence
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #Stemming - taking the root of the word
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    
    #Join
    review = ' '.join(review)
    
    corpus.append(review)
    
#Creating Bag of words model
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)

#Creating a sparse matrix to analyze the data
X = cv.fit_transform(corpus).toarray()

y = dataset.iloc[:,1]


#Now the prediction = which classification to use?

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

#---------------------------------------------------------------------------

#1. Naive Bayes
global method
method = "Naive Bayes"

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
F1_Score(cm)

#-----------------------------------------------------------------------

#2. Random Forest
method = "Random Forest"

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
F1_Score(cm)

#--------------------------------------------------------------------------

#3. Logistic Regression
method = "Logistic Regression"

#Fitting - logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train,y_train)

#Predicting the test set results
y_pred = classifier.predict(X_test)

#Evaluating the classifier performance
#Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
F1_Score(cm)