from operator import index
import pandas as pd
import numpy as np

useful_game_info = pd.read_csv("Datasets/useful_game_info.csv")
index_df = pd.read_csv("Datasets/game_indexes.csv")

def get_same_genre(game_name): #I still need to implement better way to compare genre since not all data formating is the same

    game_genre = useful_game_info.iloc[index_df[game_name]]["genre"][0]
    same_genre = []

    for i in range(len(useful_game_info["name"])):
        if np.str(useful_game_info.iloc[i]["genre"]).split(",")[0] == game_genre:
            game = useful_game_info.iloc[i]["name"]
            print(f"We got a match! {game} is same genre as {game_name}, the genre is {game_genre}")
            same_genre.append(game)
    return same_genre

print(get_same_genre("DOOM"))