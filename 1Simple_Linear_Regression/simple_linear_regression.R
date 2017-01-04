#Data Preprocessing

#Importing Dataset
dataset <- read.csv('Salary_Data.csv')
#dataset <- dataset[,2:3]

#Diving the dataset into training set and test set
library(caTools)
set.seed(123)
split <- sample.split(dataset$Salary, SplitRatio = (2/3))
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

#Feature Scaling
# training_set[,2:3] <- scale(training_set[,2:3])
# test_set[,2:3] <- scale(test_set[,2:3])


#Fitting Simple Linear Regression
regressor <- lm(formula = Salary ~ YearsExperience,
                data = training_set)
#summary(regressor)

#Prediction for the test set
y_pred <- predict(regressor,newdata = test_set)

#Visualize training set results
#install.packages(ggplot2)
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x=training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary Prediction - Training Set') +
  xlab('years of Experience') +
  ylab('Salary')

#Visualize test set results
#install.packages(ggplot2)
#library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = 'red') +
  geom_point(aes(x = test_set$YearsExperience, y = y_pred),
             color = 'blue') +
  geom_line(aes(x=training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary Prediction - Test Set') +
  xlab('years of Experience') +
  ylab('Salary')