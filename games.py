import pandas as pd
from surprise import Reader

games_df = pd.read_csv("Datasets/user.csv") #I'll try to implement games characteristic combined with Collaborative Filtering from user_df