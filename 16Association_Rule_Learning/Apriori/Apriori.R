install.packages("arules")
library(arules)

#Import Data

#dataset <- read.csv("Market_Basket_Optimisation.csv", header = FALSE)
dataset <- read.transactions("Market_Basket_Optimisation.csv", sep = ',', rm.duplicates = TRUE )
summary(dataset)
itemFrequencyPlot(dataset, topN = 100)

#Training Apriori
rules <- apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.2))

#Visualizing results
inspect(sort(rules,by='lift')[1:10])
