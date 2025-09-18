import streamlit as st
import pandas as pd
import plotly.express as px

# load the data
data = pd.read_csv("/workspaces/ds-fall-2025-fri-1230/Week-03-EDA-and-Dashboards/data/movie_ratings.csv")

#1. What's the breakdown of genres for the movies that were rated?
#get the data that has ratings only
rated_data = data.dropna(subset=["rating"])
genre_count = rated_data["genres"].value_counts(normalize=True)*100
genre_df = genre_count.reset_index()
genre_df.columns = ["Genre", "Percentage"]

st.write("### Genre Breakdown")
fig = px.bar(
    genre_df,
    x="Genre",
    y="Percentage",
    text=genre_df["Percentage"].map(lambda x: f"{x:.2f}%"),
    title="Movie Genres (Rated Only)"
)
fig.update_traces(textposition="outside")
st.plotly_chart(fig)
#2. Which genres have the highest viewer satisfaction (highest ratings)? 
st.write("Average Ratings by Genre")
average_rating = rated_data.groupby("genres")["rating"].mean()
st.write(average_rating)