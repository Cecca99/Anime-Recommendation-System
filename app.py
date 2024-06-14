import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from app_functions import get_similar_anime



with open('data/anime_summarized.pkl', 'rb') as f:
    anime_df = pickle.load(f)

embeddings = np.load('data/document_embeddings.npy')
similarity_matrix = cosine_similarity(embeddings, embeddings)

st.header('Anime Recommendation System', divider='red')
st.write("Choose the baseline anime on which you want recommendations.")
st.write("You can choose between a list of animes sorted in alphabetic order.")
st.write("After choosing the anime, you can decide how many recommendations you want.")
st.write("If you want, you can click on the *'Tell me more...'* button to have more info about the plot of the anime.")

anime = st.selectbox(label = 'Select an anime', options = sorted(list(anime_df['Name'].unique())))
number = st.selectbox(label = 'How many recommendations do you want?', options = range(2,11))

if anime and number:
  id = anime_df[anime_df['Name'] == anime].index[0]
  st.image(anime_df['Image URL'][id])
  st.write(f"**Name:** {anime}")
  st.write(f"**Genres:** {anime_df['Genres'][id]}")
  if not isinstance(anime_df['Producers'][id], float):
    st.write(f"**Producers:** {anime_df['Producers'][id]}")
  if not isinstance(anime_df['Studios'][id], float):
    st.write(f"**Studios:** {anime_df['Studios'][id]}")
  similar_animes = get_similar_anime(anime, sim_matrix = similarity_matrix, top_n = number)
  st.subheader(f'Anime similar to {anime}', divider=False)
  for similar_anime in similar_animes['Name']:
    anime_id = anime_df[anime_df['Name'] == similar_anime].index[0]
    st.image(anime_df['Image URL'][anime_id])
    st.write(f"**Name:** {similar_anime}")
    st.write(f"**Genres:** {anime_df['Genres'][anime_id]}")
    if not isinstance(anime_df['Producers'][anime_id], float):
      st.write(f"**Producers:** {anime_df['Producers'][anime_id]}")
    if not isinstance(anime_df['Studios'][anime_id], float):
      st.write(f"**Studios:** {anime_df['Studios'][anime_id]}")
    synopsis = st.write(f"**Synopsis:** {anime_df['summarized_synopsis'][anime_id]}")
    if st.button('Tell me more...', key = similar_anime):
      synopsis = st.write(f"**Synopsis:** {anime_df['Synopsis'][anime_id]}")
