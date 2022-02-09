import pandas as pd

games_df = pd.read_csv("Datasets/games.csv")
user_df = pd.read_csv("Datasets/user.csv")

#####################################################################################

useful_game_info = games_df[["name", "popular_tags", "game_details", "genre", "all_reviews"]].copy()
useful_game_info.dropna(inplace = True)
useful_game_info.to_csv("Datasets/useful_game_info.csv")

#####################################################################################

index_df = useful_game_info["name"]
index_df = index_df.T
index_df = (index_df.T.reset_index().T.reset_index(drop=True).set_axis([f'{name}' for name in useful_game_info["name"]], axis=1))
index_df.drop(1, inplace=True)
index_df.to_csv("Datasets/game_indexes.csv")

#####################################################################################

purchase_dict = {"purchase": 0, "play":1}
user_df.drop(user_df.columns[4], axis = 1, inplace = True)
user_df.columns = ["userId", "game", "purchase/play", "timePlayed"]
user_df["purchase/play"] =  user_df["purchase/play"].map(purchase_dict)

indexes = user_df[user_df["purchase/play"] ==  0].index
user_df.drop(indexes, inplace = True)
user_df.drop("purchase/play", axis = 1, inplace = True)

def create_rating(hours_played): #this need to be changed, is ambiguous
    
    if hours_played <= 1:
        return 0.0
    elif hours_played < 5:
        return 1.0
    elif hours_played < 10:
        return 2.0
    elif hours_played < 15:
        return 3.0
    elif hours_played < 20:
        return 4.0
    elif hours_played < 25:
        return 5.0
    elif hours_played < 30:
        return 6.0
    elif hours_played < 40:
        return 7.0
    elif hours_played < 50:
        return 8.0
    elif hours_played < 100:
        return 9.0
    elif hours_played >= 100:
        return 10.0

user_df["rating"] = user_df["timePlayed"].apply(create_rating)
user_df.to_csv("Datasets/user_df_with_ratings.csv")