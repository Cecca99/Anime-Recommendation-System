import pandas as pd
import pickle

with open('data/anime_summarized.pkl', 'rb') as f:
    anime_df = pickle.load(f)

def get_similar_anime(anime_name, sim_matrix, top_n=10):
    print(f'The anime most similar to {anime_name} are:')
    anime_id = anime_df[anime_df['Name'] == anime_name].index[0]
    arr = sim_matrix[anime_id]
    return anime_df[['Name']].loc[(-arr).argsort()[1:(top_n+1)]]
