import pandas as pd

games_df = pd.read_csv("Datasets/games.csv")
user_df = pd.read_csv("Datasets/user.csv")

create_useful_game_info = False
create_user_df_with_ratings = True
create_game_indexes = False

#####################################################################################

if create_useful_game_info:
    useful_game_info = games_df[["name", "popular_tags", "game_details", "genre", "all_reviews"]].copy()
    useful_game_info.dropna(inplace = True)
    useful_game_info.to_csv("Datasets/useful_game_info.csv")

#####################################################################################

if create_user_df_with_ratings:
    purchase_dict = {"purchase": 0, "play":1}
    user_df.drop(user_df.columns[4], axis = 1, inplace = True)
    user_df.columns = ["userId", "game", "purchase/play", "timePlayed"]
    user_df["purchase/play"] =  user_df["purchase/play"].map(purchase_dict)

    indexes = user_df[user_df["purchase/play"] ==  0].index
    user_df.drop(indexes, inplace = True)
    user_df.drop("purchase/play", axis = 1, inplace = True)

    average_time_played = pd.read_csv("Datasets/average_time_play_full.csv")
    average_time_played.drop("Unnamed: 0", axis = 1, inplace = True)
    average_time_played.drop("Unnamed: 0.1", axis = 1, inplace = True)

    user_df = user_df.reset_index()
    user_df.drop("index", axis = 1, inplace = True)

    row = 0
    ratings = []

    for user in user_df["userId"]:
        game = user_df.iloc[row]["game"]
        user_play_time = user_df.iloc[row]["timePlayed"]
        average_hours = average_time_played[game][0]

        if user_play_time >  1.5 * average_hours:
            rating = 5
        elif user_play_time > 1.25 * average_hours:
            rating = 4
        elif user_play_time > average_hours:
            rating = 3
        elif user_play_time > 0.75 * average_hours:
            rating = 2
        elif user_play_time > 0.5 * average_hours:
            rating = 1
        else:
            rating = 0

        ratings.append(rating)
        row += 1

    user_df["rating"] = ratings
    user_df.to_csv("Datasets/user_df_with_ratings.csv")

#####################################################################################

if create_game_indexes:
    index_df = user_df["game"].unique()
    index_df = pd.DataFrame(index_df)
    index_df = index_df.T

    index_df = (index_df.T.reset_index().T.reset_index(drop=True).set_axis([f'{name}' for name in user_df["game"].unique()], axis=1))
    index_df.drop(1, inplace=True)
    index_df.to_csv("Datasets/game_indexes.csv")