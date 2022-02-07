import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate

user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")
user_df.drop("purchase/play", axis = 1, inplace=True)
user_df.drop("Unnamed: 0", axis = 1, inplace=True)
user_df.drop("timePlayed", axis = 1, inplace=True)

rating_dict = {'itemID': list(user_df["game"]),
                'userID': list(user_df["userId"]),
                'rating': list(user_df["rating"])}

df = pd.DataFrame(rating_dict)
reader = Reader(rating_scale=(0.5, 5.0))

data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)

algo = SVD()
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)