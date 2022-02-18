import pandas as pd
import numpy as np

overwrite_data = False

user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")
main_df = pd.read_csv("Datasets/game_indexes.csv")

user_df.drop("Unnamed: 0", axis = 1, inplace=True)
user_df.drop("timePlayed", axis = 1, inplace=True)

main_df.drop("Unnamed: 0", axis = 1, inplace=True)

#I want to create user x games dataframe that contains ratings

def create_rating_vector(userId, verbose = False):

    rating_vector = []
    current_user = user_df.loc[user_df["userId"] == userId]

    for game in main_df.columns:

        if game in list(current_user["game"]):
            rating = list(current_user.loc[user_df["game"] == game]["rating"])[0]
            rating_vector.append(rating)

            if verbose:
                print(f"he played {game} and gave it a {rating}")

        else:
            rating_vector.append(np.NaN)

    
    return rating_vector
if overwrite_data:
    for user in user_df["userId"].unique():
        main_df_length = len(main_df)
        main_df.loc[main_df_length] = create_rating_vector(userId = user)
        print(main_df_length / len(user_df["userId"].unique()), "%")

    main_df.to_csv("Datasets/user_df_with_all_ratings.csv")