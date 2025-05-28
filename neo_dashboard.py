import streamlit as st
import pandas as pd
from datetime import datetime

#Load the cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_nasa_neo_data.csv")
    df['close_approach_date'] = pd.to_datetime(df['close_approach_date'])
    return df

df = load_data()

#Page title
st.title("NASA Near-Earth Object (NEO) Dashboard")
st.markdown("Explore asteroids that pass near Earth using NASA’s public API data.")

#Sidebar Filters
st.sidebar.header("Filter Options")

# Date filter
min_date = df['close_approach_date'].min().date()
max_date = df['close_approach_date'].max().date()
selected_date = st.sidebar.date_input("Select Date", value=min_date, min_value=min_date, max_value=max_date)

# Hazardous filter
hazardous_only = st.sidebar.checkbox("Show Only Hazardous Asteroids")

# Apply filters
filtered_df = df[df['close_approach_date'].dt.date == selected_date]

if hazardous_only:
    filtered_df = filtered_df[filtered_df['is_potentially_hazardous_asteroid'] == True]

st.write(f"### Asteroids on {selected_date} {'(Hazardous Only)' if hazardous_only else ''}")
st.dataframe(filtered_df)

#Sidebar Filters
st.sidebar.header("🔍 Filter Options")

# Date filter
min_date = df['close_approach_date'].min().date()
max_date = df['close_approach_date'].max().date()
selected_date = st.sidebar.date_input("Select Date", value=min_date, min_value=min_date, max_value=max_date)

# Hazardous filter
hazardous_only = st.sidebar.checkbox("Show Only Hazardous Asteroids")

# Apply filters
filtered_df = df[df['close_approach_date'].dt.date == selected_date]

if hazardous_only:
    filtered_df = filtered_df[filtered_df['is_potentially_hazardous_asteroid'] == True]

st.write(f"### Asteroids on {selected_date} {'(Hazardous Only)' if hazardous_only else ''}")
st.dataframe(filtered_df)


