import streamlit as st
import pandas as pd
import plotly.express as px

# load the data
df = pd.read_csv("/workspaces/ds-fall-2025-fri-1230/Week-03-EDA-and-Dashboards/data/movie_ratings.csv")

#1. What's the breakdown of genres for the movies that were rated?
