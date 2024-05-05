import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

import streamlit as st
import pandas as pd

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Plotting the bar chart using Streamlit's st.bar_chart()
st.bar_chart(profit_by_category.set_index('Category')['Profit'])
st.title('Profit by Category')
st.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Display the bar chart
st.write('Bar Chart: Profit by Category')

# Plotting the scatter plot using Streamlit's st.line_chart()
st.line_chart(df[['Sales', 'Profit']])
st.title('Profit vs. Sales')

# Display the scatter plot
st.write('Line Chart: Profit vs. Sales')
