import pandas as pd
from surprise import Reader, Dataset, SVD, NMF
from surprise.model_selection import cross_validate

# "This dataset is a list of user behaviors, with columns: user-id, game-title, behavior-name, value.
# The behaviors included are 'purchase' and 'play'.
# The value indicates the degree to which the behavior was performed.
# In the case of 'purchase' the value is always 1, and in the case of 'play' the value represents the number of hours the user has played the game."

purchase_dict = {"purchase": 0, "play":1}
user_df = pd.read_csv("Datasets/user.csv")
user_df.drop(user_df.columns[4], axis = 1, inplace = True)
user_df.columns = ["userId", "game", "purchase/play", "timePlayed"]
user_df["purchase/play"] =  user_df["purchase/play"].map(purchase_dict)

reader = Reader(rating_scale=(0, 1000)) #that's just my initial thought, I'm choosing that the more someone played a game the higher he rates it
data = Dataset.load_from_df(user_df[["userId", "game", "timePlayed"]], reader)

algo = SVD()
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

print("\n*******************************************************\n")
algo = NMF()
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)