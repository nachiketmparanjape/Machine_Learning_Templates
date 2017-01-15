#Thomson Sampling

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

#Number of times the ad i got reward 1 for up to round n
number_of_rewards_1 = [0] * d

#Number of times the ad i got reward 0 for up to round n
number_of_rewards_2 = [0] * d

total_reward = 0

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            #Average reward of the ad i up to n
            average_reward = (sums_of_rewards[i] / numbers_of_selections[i])
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
            
        else:
            upper_bound = 1e4000 #This loop is introduced to assign values for first 10 values
            #upper_bound = np.float64(upper_bound)                   
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    
    #Append corresponding ad to ads_selected
    ads_selected.append(ad)
    #Update number of selections for the corresponding ad
    numbers_of_selections[ad] += 1
    #Update sums of reward (use the god dataset here)
    reward = np.float64(dataset.values[n,ad])
    sums_of_rewards[ad] += reward
    total_reward += reward
    
# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()