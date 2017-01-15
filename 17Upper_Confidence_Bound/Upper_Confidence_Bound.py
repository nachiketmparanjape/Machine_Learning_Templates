#UCB Template

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#Import the dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#Implementing UCB
N = 10000 #Number of customers
d = 10 #Number of ads
ads_selected = []

#Number of times the ad i was selected up to round n
numbers_of_selections = [0] * d

#The sum of rewards of the ad i up to round n
sums_of_rewards = [0] * d

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            #Average reward of the ad i up to n
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1) / numbers_of_selections[i])
        else:
            upper_bound = 1e400
            
            upper_bound = average_reward + delta_i
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i