import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/titanic.csv")

st.title("Titanic Survival Analysis Dashboard")

# --- Data Cleaning ---
# Drop missing values in key columns
df = df.dropna(subset=['Survived', 'Pclass', 'Sex', 'Age'])

# Map numeric codes to labels
df['Survived'] = df['Survived'].map({0: 'Did Not Survive', 1: 'Survived'})
df['Pclass'] = df['Pclass'].map({1: 'First Class', 2: 'Second Class', 3: 'Third Class'})

st.subheader("Preview of Cleaned Data")
st.write(df.head())

# --- Survival Rates by Class and Gender ---
grouped = df.groupby(['Pclass', 'Sex'])['Survived'].value_counts(normalize=True).mul(100).round(2)
survival_rates = grouped.rename("Survival Rate (%)").reset_index()

st.subheader("Survival Rates by Class and Gender")
st.write(survival_rates)

# --- Age Distribution by Survival Status (Boxplot) ---
fig1, ax1 = plt.subplots(figsize=(8,6))
sns.boxplot(x='Survived', y='Age', data=df, ax=ax1)
ax1.set_title("Age Distribution by Survival Status")
st.pyplot(fig1)

# --- Average Age for Survivors vs Non-Survivors ---
avg_age = df.groupby('Survived')['Age'].mean().round(2)
st.subheader("Average Age by Survival Status")
st.write(avg_age)
