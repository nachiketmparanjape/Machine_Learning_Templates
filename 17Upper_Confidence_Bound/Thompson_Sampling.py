#Thomson Sampling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#Import the dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#Implementing UCB
N = 10000 #Number of customers
d = 10 #Number of ads
ads_selected = []

#Number of times the ad i got reward 1 for up to round n
number_of_rewards_0 = [0] * d

#Number of times the ad i got reward 0 for up to round n
number_of_rewards_1 = [0] * d

total_reward = 0

for n in range(0, N):
    ad = 0
    max_random = 0
    
    for i in range(0, d):
        
        random_beta = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
               
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    
    #Append corresponding ad to ads_selected
    ads_selected.append(ad)
    
     #Update sums of reward (use the god dataset here)
    reward = np.float64(dataset.values[n,ad])
    
    #Update number of rewards for the corresponding ad
    if reward == 1:
        number_of_rewards_1[ad] += 1
    else:
        number_of_rewards_0[ad] += 1
   
    
    total_reward += reward
    
# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()