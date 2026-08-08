import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/movies.csv")

# Drop rows with missing values in key columns
df = df.dropna(subset=['Genre', 'Rating', 'Votes', 'Year'])

st.title("Movie Ratings Explorer")

# Dropdown for genre selection
genres = df['Genre'].unique()
selected_genre = st.selectbox("Choose a genre:", genres)

# Filter data for chosen genre
genre_data = df[df['Genre'] == selected_genre]

# Summary statistics
avg_rating = genre_data['Rating'].mean()
avg_votes = genre_data['Votes'].mean()
median_year = genre_data['Year'].median()

st.subheader(f"Summary for {selected_genre}")
st.write(f"Average Rating: {avg_rating:.2f}")
st.write(f"Average Votes: {avg_votes:.0f}")
st.write(f"Median Year of Release: {median_year:.0f}")

# Boxplot of ratings across genres
fig1, ax1 = plt.subplots(figsize=(8,6))
sns.boxplot(x='Genre', y='Rating', data=df, ax=ax1)
ax1.set_title("Distribution of Ratings by Genre")
st.pyplot(fig1)

# Scatterplot Votes vs Rating for selected genre
fig2, ax2 = plt.subplots(figsize=(8,6))
sns.scatterplot(
    x='Votes', y='Rating',
    size='Votes', hue='Rating',
    data=genre_data, ax=ax2, palette="viridis", sizes=(20, 200)
)
ax2.set_title(f"Votes vs Rating for {selected_genre}")
st.pyplot(fig2)
