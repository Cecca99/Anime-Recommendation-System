# **Anime Recommendation System**

The goal of this project is to build a content based anime recommendation system, which can compare the plot of anime and return those that are most similar to the item on which suggestions are requested.\

The work done is divided into the following steps:
 * Data Acquisition
 * Exploratory Data Analysis
 * Development of a classification model that can predict the genre of anime that does not have it
 * Summarization of the synopsis in order to make the recommendation system more readable
 * Deployment of the recommendation system using *Streamlit*

The recommendation system can be found at the following link: [recommendation system](https://anime-recommendation-system-q63xpuxhspdr7oxkpqu7ah.streamlit.app/)

This repo is structured in the following way:

- **data:** This folder contains the list of animes used for the recommendation system and data processed. Specifically:
  - `anime_summarized.pkl` Contains the animes used for recommendations along with the summaries of the synopsis.
  - `animelist.csv` Original dataset retrieved from *Kaggle*.
  - `animelist_categorized.pkl` Intermediate dataset with the anime filtered but without summaries.
  - `ml_metrics.csv` Results of the cross validation process.

- **models:** This folder contains some of the models used for the analysis. Specifically:
  - `best_ml_model.pkl` Model used for the prediction of the genres.
  - `similarity_matrix.npy` Matrix that contains all the similarity values between the synopsis of the animes.

- **source code:** This folder contains all the notebooks with the code developed throughout the project. All the work was done on Google Colab. Specifically:
  - `Data Acquisition and Cleaning.ipynb` Code used for the acquisition, cleaning and filtering of the data.
  - `Document Comparison.ipynb` Code used for the vectorization of the documents and the building of the similarity matrix.
  - `EDA.ipynb` Code used for Exploratory Data Analysis.
  - `Genre Prediction.ipynb` Code used for the inference of the genres.
  - `Recommendation System.ipynb` Code used to develop and test the recommendation system.
  - `Text Classification.ipynb` Code used for training, optimizing and testing of the classification models.
  - `Text Summarization.ipynb` Code used for building and evaluate the summaries.

- `app.py` Python code of the recommendation system.
- `app_functions.py` Useful functions to make the recommendation system work properly.

