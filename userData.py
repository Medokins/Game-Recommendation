import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

# "This dataset is a list of user behaviors, with columns: user-id, game-title, behavior-name, value.
# The behaviors included are 'purchase' and 'play'.
# The value indicates the degree to which the behavior was performed.
# In the case of 'purchase' the value is always 1, and in the case of 'play' the value represents the number of hours the user has played the game."

purchase_dict = {"purchase": 0, "play":1} #this might be usefull in the future
user_df = pd.read_csv("Datasets/user.csv")
user_df.drop(user_df.columns[4], axis = 1, inplace = True)
user_df.columns = ["userId", "game", "purchase/play", "timePlayed"]
user_df["purchase/play"] =  user_df["purchase/play"].map(purchase_dict)

user_favourites = user_df.pivot_table(index=['userId'], columns=['game'], values='timePlayed')
user_favourites.fillna(0, inplace = True)

game_similarity = cosine_similarity(user_favourites.T)
game_similarity_df = pd.DataFrame(game_similarity, index=user_df["game"].unique(), columns = user_df["game"].unique())

def get_similar_games(game_name, user_raiting):
    similar_games = game_similarity_df[game_name] * (user_raiting-50)
    similar_games = similar_games.sort_values(ascending=False)

    return similar_games

print(get_similar_games("Quake", 100))