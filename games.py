import pandas as pd

useful_game_info = pd.read_csv("Datasets/useful_game_info.csv")
index_df = pd.read_csv("Datasets/game_indexes.csv")


def get_same_genre(game_name, verbose=False, opinion_factored=True):

    same_genre = []
    game_genre = useful_game_info.iloc[index_df[game_name][0]]["genre"].split(",")[0]

    if opinion_factored:
        opinion_dict = {"Overwhelmingly Positive": 2, "Very Positive": 1.5, "Mostly Positive": 1, "Positive":1, "Mixed":0, "Negative":-1, "Very Negative":-1, "Mostly Negative":-1, "Overwhelmingly Negative":-1}

    for i in range(len(useful_game_info["name"])):
        current_genre = useful_game_info.iloc[i]["genre"].split(",")[0]
        if current_genre == game_genre:
            game = useful_game_info.iloc[i]["name"]
            if opinion_factored:
                opinion = useful_game_info.iloc[i]["all_reviews"].split(",")[0]
                if opinion in opinion_dict and opinion_dict[opinion] >= 1:
                    same_genre.append(game)
                    if verbose:
                        print(f"We got a match! {game} is same genre as {game_name} and have {opinion} reviews")
            else:
                same_genre.append(game)
                if verbose:
                    print(f"We got a match! {game} is same genre as {game_name}, the genre is {current_genre}")

    return same_genre

get_same_genre("Grand Theft Auto IV", verbose=True, opinion_factored=True)