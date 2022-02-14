import pandas as pd
import numpy as np

#I found https://github.com/ckatzorke/howlongtobeat api which i wanted to use to better implement rating based on user play time vs avarage play time to beat game
#average time played in this dataset vs user time played should do it instead of this ^ (because more than 30% of games in my dataset are missing on this page + it has different formating)

train = False

if train:
    useful_game_info = pd.read_csv("Datasets/user_df_with_ratings.csv")
    main_df = pd.read_csv("Datasets/game_indexes.csv")
    average_time_played = main_df.copy()

    counter = 0 #I trained it in patches of 500 because it was taking very long time to complete
    num_of_columns = len(main_df.columns)
    for game in main_df.columns[1:]:

        number_of_players = 0
        summ_of_hours = 0
        percent = counter / num_of_columns
        print(f"Currently on {percent}%")
        counter += 1

        for row in range(len(useful_game_info["game"])):
            if useful_game_info.iloc[row]["game"] == game:
                #print(f"Found {game} in row nr {row}")
                number_of_players += 1
                summ_of_hours += useful_game_info.iloc[row]["timePlayed"]

        average_time_played[game][0] = summ_of_hours / np.float(number_of_players)
        average_time_played.to_csv(f"Datasets/average_time_play_{counter}.csv")