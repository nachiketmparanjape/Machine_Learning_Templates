#Natural Language Processing

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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