# Game-Recommendation

This is my first project using Collaborative Filtering.

I chose surprise packet for implementing Collaborative Filtering based on user similarty, cosine_similarity from sklearn for implementing Collaborative Filtering based on item similiarty and two Kaggle datasets for games and user data. I also created rating column which is based on average time played by users in this dataset vs the user play time.

Collaborative Filtering based on item similarity is completed and working pretty well in my opinion.

Collaborative Filtering based on user similarity is still in progess I took another approach to the problem in V2 version yet I need to read some more lecture on it.
Currently, the algorithm is working but I think I messed up similarity matrix since I trated it as a square matix (3600x3600) when in reality it's 11124x3600.