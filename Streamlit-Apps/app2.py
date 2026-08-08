import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Inject custom CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffb6c1; /* Light blue background */
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

#Load Dataset
df = pd.read_csv("data/grades.csv")


st.title("Student Grades Explorer")

st.subheader("Preview Data")
st.write(df.head())

#Dropdown for subject selection
subjects= df['Subject'].unique()
selected_subject = st.selectbox("Choose a subject:", subjects)

#Filter data for chosen subject
subject_data = df[df['Subject'] == selected_subject]

#Summary statistics
mean_score = subject_data['Final'].mean()
median_score = subject_data['Final'].median()
std_score = subject_data['Final'].std()

st.subheader(f"Summary for {selected_subject}")
st.write(f"Mean: {mean_score:.2f}")
st.write(f"Median: {median_score:.2f}")
st.write(f"Std Dev: {std_score:.2f}")

# Boxplot across subjects
fig1, ax1 = plt.subplots(figsize=(8,6))
sns.boxplot(x='Subject', y='Final', data=df, ax=ax1)
ax1.set_title("Final Score Distribution by Subject")
st.pyplot(fig1)

# Scatterplot Test1 vs Final
fig2, ax2 = plt.subplots(figsize=(8,6))
sns.scatterplot(x='Test1', y='Final', hue='Subject', data=df, ax=ax2)
ax2.set_title("Test1 vs Final Scores by Subject")
st.pyplot(fig2)
