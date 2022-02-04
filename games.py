import pandas as pd

games_df = pd.read_csv("Datasets/games.csv") #Plan is to implement games characteristic combined with Collaborative Filtering from user_df
index_df = pd.DataFrame(games_df["name"])

index_df = index_df.T
index_df = (index_df.T.reset_index().T.reset_index(drop=True)
            .set_axis([f'{name}' for name in games_df["name"]], axis=1))
index_df.drop(1, inplace=True)

useful_game_info = games_df[["name", "popular_tags", "game_details", "genre", "all_reviews"]].copy()
useful_game_info.dropna(inplace = True)

#I need to drop some rows, some games have inccorect data format

def get_same_genre(game_name):
    game_genre = useful_game_info.iloc[index_df[game_name]]["genre"][0]
    most_popular_tag = useful_game_info.iloc[index_df[game_name]]["popular_tags"][0].split(",")[0]
    same_genre = []
    for game in useful_game_info["name"]:
        print(game)
        print(useful_game_info.iloc[index_df[game]])
        # if useful_game_info.iloc[index_df[game]]["genre"][0] == game_genre or useful_game_info.iloc[index_df[game]]["popular_tags"][0].split(",")[0] == most_popular_tag:
        #     same_genre.append(game)
    return same_genre

print(get_same_genre("DOOM"))