import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# "This dataset is a list of user behaviors, with columns: user-id, game-title, behavior-name, value.
# The behaviors included are 'purchase' and 'play'.
# The value indicates the degree to which the behavior was performed.
# In the case of 'purchase' the value is always 1, and in the case of 'play' the value represents the number of hours the user has played the game."

purchase_dict = {"purchase": 0, "play":1} #this might be useful in the future
user_df = pd.read_csv("Datasets/user.csv")
user_df.drop(user_df.columns[4], axis = 1, inplace = True)
user_df.columns = ["userId", "game", "purchase/play", "timePlayed"]
user_df["purchase/play"] =  user_df["purchase/play"].map(purchase_dict)

def create_rating(hours_played): #this need to be fixed bcs right now it is very ambiguous
    if hours_played <= 1:
        return 0.0
    elif hours_played < 10:
        return 1.0
    elif hours_played < 25:
        return 2.0
    elif hours_played < 50:
        return 3.0
    elif hours_played < 150:
        return 4.0
    elif hours_played >= 150:
        return 5.0

def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row

user_df["rating"] = user_df["timePlayed"].apply(create_rating)
#user_df.to_csv("Datasets/user_df_with_ratings.csv")

user_favourites = user_df.pivot_table(index=['userId'], columns=['game'], values='rating')
user_favourites = user_favourites.apply(standardize)
user_favourites.fillna(0, inplace = True)

game_similarity = cosine_similarity(user_favourites.T)
game_similarity_df = pd.DataFrame(game_similarity, index=user_df["game"].unique(), columns = user_df["game"].unique())

def get_similar_games(game_name, user_raiting):
    similar_games = game_similarity_df[game_name] * (user_raiting - 1.0)
    similar_games = similar_games.sort_values(ascending=False)

    return similar_games

print(get_similar_games("Borderlands 2", 3))