import pandas as pd
from surprise import Reader

# "This dataset is a list of user behaviors, with columns: user-id, game-title, behavior-name, value.
# The behaviors included are 'purchase' and 'play'.
# The value indicates the degree to which the behavior was performed.
# In the case of 'purchase' the value is always 1, and in the case of 'play' the value represents the number of hours the user has played the game."

user_df = pd.read_csv("Datasets/user.csv")