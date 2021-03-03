install.packages("recommenderlab")
library(recommenderlab)
library(readr)
library(readxl)
install.packages("reshape2")
library(reshape2)

game_data <- read.csv("F:\\assignment\\recommondation system\\Datasets_Recommendation Engine\\game.csv",header = TRUE)
head(game_data)
game_data <- game_data[,1:3]
head(game_data)
dim(game_data)
## covert to matrix format

game_matrix <- as.matrix(acast(game_data,game~rating,fun.aggregate = mean))
dim(game_matrix)        

## recommendarlab realRatingMatrix format

R <- as(game_matrix, "realRatingMatrix")

rec1 <- Recommender(R, method="UBCF")  ## User-based collaborative filtering                       
rec2 = Recommender(R, method="IBCF") ## Item-based collaborative filtering
rec3 = Recommender(R, method="SVD")
rec4 = Recommender(R, method="POPULAR")
rec5 = Recommender(binarize(R,minRating=2), method="UBCF") ## binarize all 2+ rating to 1

## create n recommendations for a user
uid = "3.5"
games <- subset(game_data, game_data$rating==uid)
print("You have rated:")
games
print("recommendations for you:")
prediction <- predict(rec1, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec2, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec3, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec4, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec5, R[uid], n=2) ## you may change the model here
as(prediction, "list")

################################# problem 2 ######################################
install.packages("recommenderlab")
library(recommenderlab)
library(readr)
library(readxl)
install.packages("reshape2")
library(reshape2)

ent_data <- read.csv("F:\\assignment\\recommondation system\\Datasets_Recommendation Engine\\Entertainment.csv",header = TRUE)
head(ent_data)
ent_data <- ent_data[,1:3]
head(ent_data)
dim(ent_data)
## covert to matrix format

ent_matrix <- as.matrix(acast(ent_data,Titles~Category,fun.aggregate = mean))
dim(ent_matrix)        

## recommendarlab realRatingMatrix format

R <- as(ent_matrix, "realRatingMatrix")

rec1 <- Recommender(R, method="UBCF")  ## User-based collaborative filtering                       
rec2 = Recommender(R, method="IBCF") ## Item-based collaborative filtering
rec3 = Recommender(R, method="SVD")
rec4 = Recommender(R, method="POPULAR")
rec5 = Recommender(binarize(R,minRating=2), method="UBCF") ## binarize all 2+ rating to 1

## create n recommendations for a user
uid = "Action, Comedy, Historical, Parody, Samurai, Sci-Fi, Shounen"
enta <- subset(ent_data, ent_data$Category==uid)
print("You have rated:")
enta
print("recommendations for you:")
prediction <- predict(rec1, R[uid], n=1) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec2, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec3, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec4, R[uid], n=2) ## you may change the model here
as(prediction, "list")
prediction <- predict(rec5, R[uid], n=2) ## you may change the model here
as(prediction, "list")
