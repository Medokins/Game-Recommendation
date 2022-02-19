import pandas as pd
import numpy as np
import scipy.stats

overwrite_data = False
normalize_ratings = False

if overwrite_data:
    user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")
    main_df = pd.read_csv("Datasets/game_indexes.csv")

    user_df.drop("Unnamed: 0", axis = 1, inplace=True)
    user_df.drop("timePlayed", axis = 1, inplace=True)
    main_df.drop("Unnamed: 0", axis = 1, inplace=True)

if normalize_ratings:
    user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")
    ratings_df = pd.read_csv("Datasets/user_df_with_all_ratings.csv")
    ratings_df.drop("Unnamed: 0", axis = 1, inplace=True)

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
        print(main_df_length / len(user_df["userId"].unique()) * 100, "%")
    main_df.to_csv("Datasets/user_df_with_all_ratings.csv")

if normalize_ratings:
    ratings_df.drop([0], axis = 0, inplace=True)
    ratings_df['userId'] = user_df['userId'].unique()
    ratings_df.set_index('userId', inplace=True)

    def normalize(dataframe):
        dataframe_mean = dataframe.mean(axis=1)
        return dataframe.subtract(dataframe_mean, axis = 0)

    ratings_df = normalize(ratings_df)
    ratings_df.to_csv("Datasets/user_df_with_all_ratings_normalized.csv")


#I'm using scipy which has it own normalization method so im leaving normalized ratings for now

ratings_df = pd.read_csv("Datasets/user_df_with_all_ratings.csv")
#ratings_df.set_index('userId', inplace=True)
ratings_df.drop('userId', axis=1, inplace=True)

users = len(ratings_df)
games = len(ratings_df.columns)

similarity_matrix = []

for i in range(users):
    for j in range(games):
        x, y = ratings_df.iloc[i,:].values, ratings_df.iloc[j,:].values

        nas = np.logical_or(np.isnan(x), np.isnan(y))
        print(f"X:{x[~nas]}\nY:{y[~nas]}")
        print(f"len of X:{len(x[~nas])}, len of Y:{len(y[~nas])}")
        corr = scipy.stats.pearsonr(x[~nas], y[~nas])[0]
        print(f"Correlation:{corr}\n**************************************************\n")
        similarity_matrix.append(corr)

similarity_matrix = np.array(similarity_matrix)
similarity_df = pd.DataFrame(data = similarity_matrix.reshape(len(ratings_df), len(ratings_df.columns)))
similarity_df.to_csv("Datasets/similarity_matrix.csv")