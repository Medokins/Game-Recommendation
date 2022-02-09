import pandas as pd

# I found https://github.com/ckatzorke/howlongtobeat api which i will use to better implement rating based on user play time + avarage play time to beat game
#average time played vs user time played should do it instead of this ^ (bcs more than 30% of games in my dataset are missing on this page + it has different formating)

useful_game_info = pd.read_csv("Datasets/useful_game_info.csv")

average_time_played = useful_game_info["name"]
average_time_played = average_time_played.T
average_time_played = (average_time_played.T.reset_index().T.reset_index(drop=True).set_axis([f'{name}' for name in useful_game_info["name"]], axis=1))
average_time_played.drop(1, inplace=True)

for column in average_time_played:
    average_time_played[column] = 1  #put average time played here in future

print(average_time_played.head())