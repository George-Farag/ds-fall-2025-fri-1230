import streamlit as st
import pandas as pd
import plotly.express as px

# load the data
data = pd.read_csv("/workspaces/ds-fall-2025-fri-1230/Week-03-EDA-and-Dashboards/data/movie_ratings.csv")
st.set_page_config(page_title="Movie Ratings Dashboard")
#1. What's the breakdown of genres for the movies that were rated?
st.write("Question 1")
rated_data = data.dropna(subset=["rating"])
genre_count = rated_data["genres"].value_counts(normalize=True) * 100
genre_df = genre_count.reset_index()
genre_df.columns = ["Genre", "Percentage"]

fig = px.bar(
    genre_df,
    x="Genre",
    y="Percentage",  
    text=genre_df["Percentage"].map(lambda x: f"{x:.3f}%"),
    title="Rating per movie genre",
    color_discrete_sequence=["#0964A0"]
)
fig.update_traces(textposition="outside")
st.plotly_chart(fig)

#2. Which genres have the highest viewer satisfaction (highest ratings)? 
st.write("Question 2")
avg_rating = rated_data.groupby("genres")["rating"].mean().round(2).reset_index()
avg_rating.columns = ["Genre", "Average Rating"]

fig = px.bar(
    avg_rating.sort_values("Average Rating", ascending=False),
    x="Genre",
    y="Average Rating",
    text="Average Rating",
    title="Average Viewer Rating per Genre",
    color="Average Rating",
    color_continuous_scale="Blues",
    height = 500
)

fig.update_traces(textposition="outside")
st.plotly_chart(fig)

#3. How does mean rating change across movie release years?
st.write("Question 3")
yearly_ratings = rated_data.dropna(subset=["year"])

yearly_avg = (
    yearly_ratings.groupby("year")["rating"]
    .mean()
    .round(2)
    .reset_index()
)

yearly_avg.columns = ["Year", "Average Rating"]

fig = px.line(
    yearly_avg,
    x="Year",
    y="Average Rating",
    markers=True,
    title="Average Viewer Rating by Release Year",
)

fig.update_traces(
    line=dict(color="#0964A0", width=3),
    marker=dict(color="#FFFFFF", size=8)
)
st.plotly_chart(fig)

#4. What are the 5 best-rated movies that have at least 50 ratings? At least 150 ratings?
st.write("Question 4")
movie_stats = rated_data.groupby("title").agg(
    avg_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()

# Top 5 movies with at least 50 ratings
top50 = (
    movie_stats[movie_stats["rating_count"] >= 50]
    .sort_values("avg_rating", ascending=False)
    .head(5)
)

fig1 = px.bar(
    top50,
    x="title",
    y="avg_rating",
    text=top50["avg_rating"].round(2),
    title="Top 5 Movies (with at least 50 ratings)",
    color="avg_rating",
    color_continuous_scale="Blues",
    height=600
)
fig1.update_traces(textposition="outside")
st.plotly_chart(fig1)

# Top 5 movies with at least 150 ratings
top150 = (
    movie_stats[movie_stats["rating_count"] >= 150]
    .sort_values("avg_rating", ascending=False)
    .head(5)
)

fig2 = px.bar(
    top150,
    x="title",
    y="avg_rating",
    text=top150["avg_rating"].round(2),
    title="Top 5 Movies (with at least 150 ratings)",
    color="avg_rating",
    color_continuous_scale="Blues",
    height=600
)
fig2.update_traces(textposition="outside")
st.plotly_chart(fig2)