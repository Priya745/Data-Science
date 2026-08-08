import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Inject custom CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f8ff; /* Light blue background */
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("Retail Sales Dashboard")

# Load dataset
df = pd.read_csv("data/sales.csv")
st.subheader("Preview Data")
st.write(df.head())

# Summary statistics
st.subheader("Daily Revenue Summary")
st.write("Mean:", df['Revenue'].mean())
st.write("Median:", df['Revenue'].median())

# Group by product category
st.subheader("Revenue by Product Category")
grouped = df.groupby('ProductCategory').agg({'UnitsSold':'sum','Revenue':'sum'})
st.write(grouped)

# Line chart: daily revenue trend
st.subheader("Daily Revenue Trend")
st.line_chart(df.set_index('Date')['Revenue'])

# Bar chart: revenue by category
st.subheader("Revenue by Category")
st.bar_chart(grouped['Revenue'])

