#Data Preprocessing

#Importing Dataset
dataset <- read.csv('Position_Salaries.csv')
dataset <- dataset[,2:3]

#Fitting Linear Regression Model
lin_reg <- lm(formula = Salary ~ Level,
              data = dataset)
summary(lin_reg)

#Fitting Polynomial Regression Model
dataset$Level2 <- dataset$Level^2
dataset$Level3 <- dataset$Level^3
poly_reg <- lm(formula = Salary ~ .,
               data = dataset)
summary(poly_reg)

#Visualize Linear Regression
library(ggplot2)
  ggplot()  +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), colour = 'blue') +
    ggtitle("truth or bluff - linear regression") +
    xlab("Level") +
    ylab("Salary")
  
#Visualize Polynomial Regression
  ggplot()  +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), colour = 'blue') +
    ggtitle("truth or bluff - polynomial regression") +
    xlab("Level") +
    ylab("Salary")
  
#Predict new salary with linear regression
  y_pred <- predict(lin_reg, data.frame(Level=6.5))
  
#Predict new salary with polynomial regression
  y_pred <- predict(poly_reg, data.frame (Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3))
