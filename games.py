import pandas as pd
import numpy as np

useful_game_info = pd.read_csv("Datasets/useful_game_info.csv")
index_df = pd.read_csv("Datasets/game_indexes.csv")

def get_same_genre(game_name, verbose=False):

    same_genre = []
    game_genre = useful_game_info.iloc[index_df[game_name][0]]["genre"].split(",")[0]

    for i in range(len(useful_game_info["name"])):
        current_genre = useful_game_info.iloc[i]["genre"].split(",")[0]
        if current_genre == game_genre:
            game = useful_game_info.iloc[i]["name"]
            same_genre.append(game)
            if verbose:
                print(f"We got a match! {game} is same genre as {game_name}, the genre is {current_genre}")

    return same_genre

print(get_same_genre("The Elder Scrolls®: Legends™"))