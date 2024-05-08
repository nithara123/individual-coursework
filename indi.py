import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

# Load your dataset into a pandas DataFrame (replace 'your_dataset.csv' with your actual CSV file)
df = pd.read_csv('https://github.com/nithara123/individual-coursework/blob/main/cleaned_dataset.csv')

# Display the DataFrame
st.write("Initial data:")
st.write(df.head())

# Bar graph - Sales by Category
sales_by_category = df.groupby('Category')['Quantity'].sum()
st.subheader('Bar Graph - Sales by Category')
fig_bar = plt.figure(figsize=(8, 6))
sales_by_category.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.title('Bar Graph - Sales by Category')
st.pyplot(fig_bar)

# Line graph - Sales Over Time
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_over_time = df.groupby(pd.Grouper(key='Order Date', freq='M')).sum()['Sales']
st.subheader('Line Graph - Sales Over Time')
fig_line = plt.figure(figsize=(10, 6))
sales_over_time.plot(kind='line')
plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.title('Line Graph - Sales Over Time')
st.pyplot(fig_line)

# Histogram - Sales Quantity Distribution
st.subheader('Histogram - Sales Quantity Distribution')
fig_hist = plt.figure(figsize=(8, 6))
df['Quantity'].plot(kind='hist', bins=10)
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Histogram - Sales Quantity Distribution')
st.pyplot(fig_hist)
