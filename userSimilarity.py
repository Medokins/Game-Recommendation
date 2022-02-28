import pandas as pd

current_player = 100
treshold = 0.25 #value from -1.0 to 1.0, the higher it is the more selective algorithm will be

similarity_df = pd.read_csv("Datasets/similarity_df.csv")
similarity_df.drop("Unnamed: 0", axis = 1, inplace=True)

game_indexes_inverted = pd.read_csv("Datasets/game_indexes_inverted.csv")
game_indexes_inverted.drop("Unnamed: 0", axis = 1, inplace=True)

ratings_df = pd.read_csv("Datasets/user_df_with_ratings.csv")
ratings_df.drop("Unnamed: 0", axis = 1, inplace=True)

user_indexes = pd.read_csv("Datasets/user_indexes_inverted.csv")
user_indexes.drop("Unnamed: 0", axis = 1, inplace=True)

###########################################################################

def neighbours(sim):
   return [sim.index[i] for i, v in enumerate(sim) if (v>=treshold)]
similar_players = neighbours(similarity_df.iloc[current_player])

if str(current_player) in similar_players:
    similar_players.remove(str(current_player))

###########################################################################

similar_players_Ids = []
for player in similar_players:
    similar_players_Ids.append(user_indexes[player][0])

###########################################################################

def get_current_player_games(index):
    active_player_id = user_indexes[str(index)][0]
    active_player = ratings_df.loc[ratings_df["userId"] == active_player_id]
    active_player = active_player["game"]
    active_player_games = []

    for row in range(len(active_player)):
        game = active_player.iloc[row]
        if game not in active_player_games:
            active_player_games.append(game)

    return active_player_games

###########################################################################

active_player_games = get_current_player_games(current_player)
recommended_games = []
super_recommended = []

for player in similar_players_Ids:

    current_player = ratings_df.loc[ratings_df["userId"] == player]
    player_recommendation = current_player.loc[current_player['rating'] >= 4]['game']

    for row in range(len(player_recommendation)):
        game = player_recommendation.iloc[row]

        if game not in active_player_games:
            if game not in recommended_games:
                recommended_games.append(game)
            else:
                super_recommended.append(game)

if len(super_recommended) == 0:
    if len(recommended_games) != 0:
        print(f"Users similar to You liked: {recommended_games}")
    else:
        print(f"Woah, You're quite unique, there is noone like You (at current treshold: {treshold})")
else:
    print(f"Multiple players similar to You liked {super_recommended}")