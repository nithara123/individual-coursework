import streamlit as st
import pandas as pd

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Custom color palette for the bar chart
bar_colors = ['#003399', '#99CCFF', '#CCCCCC']

# Plotting the bar chart with custom colors
st.bar_chart(profit_by_category.set_index('Category')['Profit'], use_container_width=True, color=bar_colors)

# Display the bar chart title
st.title('Profit by Category')

# Display the bar chart with rotated x-axis labels for better readability
st.write('Bar Chart: Profit by Category')

# Custom color for the scatter plot
scatter_color = 'blue'

# Plotting the scatter plot with custom color
st.line_chart(df[['Sales', 'Profit']], use_container_width=True, line_width=2, color=scatter_color)

# Display the scatter plot title
st.title('Profit vs. Sales')

# Display the scatter plot
st.write('Line Chart: Profit vs. Sales')

