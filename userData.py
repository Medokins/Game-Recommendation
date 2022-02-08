import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# "This dataset is a list of user behaviors, with columns: user-id, game-title, behavior-name, value.
# The behaviors included are 'purchase' and 'play'.
# The value indicates the degree to which the behavior was performed.
# In the case of 'purchase' the value is always 1, and in the case of 'play' the value represents the number of hours the user has played the game."

# THIS IS INNACURATE, SO I WILL NOT USE THIS, LEAVING CODE FOR FUTURE LEARNING PURPOUSE

user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")

def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row

user_favourites = user_df.pivot_table(index=['userId'], columns=['game'], values='rating')
user_favourites = user_favourites.apply(standardize)
user_favourites.fillna(0, inplace = True)

game_similarity = cosine_similarity(user_favourites.T)
game_similarity_df = pd.DataFrame(game_similarity, index=user_df["game"].unique(), columns = user_df["game"].unique())

def get_similar_games(game_name, user_raiting):
    similar_games = game_similarity_df[game_name] * (user_raiting - 1.0)
    similar_games = similar_games.sort_values(ascending=False)

    return similar_games

print(get_similar_games("Borderlands 2", 5))