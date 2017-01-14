#Hierarchical Clustering Template

#Import data
dataset <- read.csv("Mall_Customers.csv")
X <- dataset[4:5]

#Using Dendrograms to find optimal number of clusters
dendrogram <- hclust(dist(X, method = 'euclidean'), method = 'ward.D')
plot(dendrogram,
     main = paste("Dendrogram"),
     xlab = "Customers",
     ylab = "Euclidean Distances")

#Fitting
hc <- hclust(dist(X, method = 'euclidean'), method = 'ward.D')
y_hc <- cutree(hc, 5)

#Visualization
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste("Clusters of Clients"),
         xlab = 'Annual Income',
         ylab = 'Spending Score')
