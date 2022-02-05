import pandas as pd

games_df = pd.read_csv("Datasets/games.csv")
index_df = pd.DataFrame(games_df["name"])

index_df = index_df.T
index_df = (index_df.T.reset_index().T.reset_index(drop=True)
            .set_axis([f'{name}' for name in games_df["name"]], axis=1))
index_df.drop(1, inplace=True)

useful_game_info = games_df[["name", "popular_tags", "game_details", "genre", "all_reviews"]].copy()
useful_game_info.dropna(inplace = True)
useful_game_info.to_csv("Datasets/useful_game_info.csv")
index_df.to_csv("Datasets/game_indexes.csv")