import pandas as pd
from surprise import Reader

games_df = pd.read_csv("Datasets/games.csv") #Plan is to implement games characteristic combined with Collaborative Filtering from user_df
index_df = pd.DataFrame(games_df["name"])

# print(games_df["name"].head(1)) #using this as id
# print(games_df["all_reviews"].head(1)) #maby useful
# print(games_df["popular_tags"].head(1)) #useful
# print(games_df["game_details"].head(1)) #useful
# print(games_df["genre"].head(1)) #useful

index_df = index_df.T
index_df = (index_df.T.reset_index().T.reset_index(drop=True)
            .set_axis([f'{name}' for name in games_df["name"]], axis=1))
index_df.drop(1, inplace=True)

useful_game_info = games_df[["name", "popular_tags", "game_details", "genre", "all_reviews"]].copy()

print(useful_game_info.iloc[index_df["Dishonored®: Death of the Outsider™"]]) #example, will be usefull when I combine this wither user_df