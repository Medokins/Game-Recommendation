import pandas as pd

games_df = pd.read_csv("Datasets/games.csv")
user_df = pd.read_csv("Datasets/user.csv")

create_useful_game_info = False
create_user_df_with_ratings = False
create_game_indexes = False
create_game_indexes_inverted = False
create_user_indexes = False
create_user_indexes_inverted = False
create_similarity_matrix = False

overwrite_data = False
normalize_ratings = False

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

######################################################################################

if create_game_indexes_inverted:
    game_indexes = pd.read_csv("Datasets/game_indexes.csv")
    game_indexes.drop("Unnamed: 0", axis = 1, inplace=True)

    games = game_indexes.columns
    indexes = [i for i in range(len(games))]

    game_indexes_inverted = pd.DataFrame(games, index=indexes, columns=["game"])
    game_indexes_inverted = game_indexes_inverted.T
    game_indexes_inverted.to_csv("Datasets/game_indexes_inverted.csv")

#######################################################################################

if create_user_indexes:

    user_df = pd.read_csv("Datasets/user_df_with_ratings.csv")

    index_df = user_df["userId"].unique()
    index_df = pd.DataFrame(index_df)
    index_df = index_df.T

    index_df = (index_df.T.reset_index().T.reset_index(drop=True).set_axis([f'{name}' for name in user_df["userId"].unique()], axis=1))
    index_df.drop(1, inplace=True)
    index_df.to_csv("Datasets/user_indexes.csv")

#######################################################################################

if create_user_indexes_inverted:
    user_indexes = pd.read_csv("Datasets/user_indexes.csv")
    user_indexes.drop("Unnamed: 0", axis = 1, inplace=True)

    users = user_indexes.columns
    indexes = [i for i in range(len(users))]

    user_indexes_inverted = pd.DataFrame(users, index=indexes, columns=["userId"])
    user_indexes_inverted = user_indexes_inverted.T
    user_indexes_inverted.to_csv("Datasets/user_indexes_inverted.csv")

########################################################################################

if create_similarity_matrix:

    import scipy.stats
    import numpy as np

    ratings_df = pd.read_csv("Datasets/user_df_with_all_ratings.csv")
    ratings_df.drop('userId', axis=1, inplace=True)
    ratings_df.fillna(99, inplace=True)

    def similarity_pearson(x, y):
        return scipy.stats.pearsonr(x, y)[0]

    users = len(ratings_df)
    similarity_matrix = []

    for i in range(users):

        for j in range(users):
            similarity_matrix.append(similarity_pearson(ratings_df.iloc[i,:], ratings_df.iloc[j,:]))    

        if i%1000 == 0:
            print(f"Currently:{(i*users + j) / (users*users) * 100}%")
            textfile = open("backup_file.txt", "w")
            for element in similarity_matrix:
                textfile.write(str(element) + " ")
            textfile.close()
    
    similarity_matrix = np.array(similarity_matrix)

    similarity_df = pd.DataFrame(data = similarity_matrix.reshape(users, users))
    similarity_df.to_csv("Datasets/users_similarity_df.csv")

#########################################################################################

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