from steamUser import steamUser
import pandas as pd

# Initialize the steamUser class with the user's SteamID and your Steam API Key
# This API Key is invalid, make sure you are using a valid one
userSteamId = "Your STEAM user Id"
API_Key = "Your STEAM Api Key"
verbose = False

###################################################################################

user = steamUser(userSteamId, API_Key)
gameCount, userGames = user.getGames()

games = pd.read_csv("../Datasets/game_indexes.csv")
games.drop("Unnamed: 0", axis = 1, inplace=True)
game_list = games.columns.tolist()

average_play_time = pd.read_csv("../Datasets/average_time_play_full.csv")
average_play_time.drop("Unnamed: 0", axis = 1, inplace=True)
average_play_time.drop("Unnamed: 0.1", axis = 1, inplace=True)

game_similarity_df = pd.read_csv("../Datasets/game_similarity_df.csv")
game_similarity_df.set_index('game', inplace=True)

favorite_games = []

for game in userGames:

    name = game["name"]
    playtime = game["playtime"]

    if name in game_list:

        average_hours = average_play_time[name][0]

        if playtime >  1.5 * average_hours:
            rating = 5
        elif playtime > 1.25 * average_hours:
            rating = 4
        elif playtime > average_hours:
            rating = 3
        elif playtime > 0.75 * average_hours:
            rating = 2
        elif playtime > 0.5 * average_hours:
            rating = 1
        else:
            rating = 0

        if rating >= 4:

            favorite_games.append([name, rating])
            if verbose:
                print(f"You really like {name} (rating: {rating})")

        else:
            if verbose:
                print(f"You seem to have played {name} but didn't really like it (rating: {rating})")

    else:
        if verbose:
            print(f"{name} is not in my Dataset")

def get_similar_games(game_name, user_raiting):
    similar_games = game_similarity_df[game_name] * (user_raiting - 1.0)
    similar_games = similar_games.sort_values(ascending=False)

    return similar_games


for title in favorite_games:

    game = title[0]
    user_rating = title[1]

    games = get_similar_games(game, user_rating)
    games = pd.DataFrame(games)
    games.reset_index(inplace=True)

    print(f"because You liked {game} You might like: ", games["game"][1])