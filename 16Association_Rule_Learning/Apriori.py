#Apriori Template

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import the data
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

#Create a list of lists to feed it to the function
transactions = []
for i in range(len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
#Train Apriori Model
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)  

#Visualization
results = list(rules)