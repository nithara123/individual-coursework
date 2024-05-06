import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Set up the layout
st.set_page_config(layout="wide")

# Define custom colors
colors = ['lightgreen', 'darkgreen', 'gray', 'black']

# First row: Profit vs. Sales Line Chart and Top 10 Customers by Total Profit Pie Chart
col1, col2 = st.columns([2, 1])

# Display the topic of the first row
col1.markdown("### Profit vs. Sales")

# Plotting the scatter plot for Profit vs. Sales
with col1:
    st.line_chart(df[['Sales', 'Profit']], width=300, height=200)  # Adjusted width and height

# Group the data by Customer ID and Product Category, and calculate the total profit
customer_preferences = df.groupby(['Customer ID', 'Category'])['Profit'].sum().reset_index()

# Pivot the data to have Customer ID as rows, Product Categories as columns, and Profit as values
pivot_table = customer_preferences.pivot(index='Customer ID', columns='Category', values='Profit').fillna(0)

# Calculate total profit for each customer
pivot_table['Total Profit'] = pivot_table.sum(axis=1)

# Sort customers by total profit in descending order
sorted_customers = pivot_table.sort_values(by='Total Profit', ascending=False)

# Select top 10 customers based on total profit
top_customers = sorted_customers.head(10)

# Display the topic of the first row
col2.markdown("### Top 10 Customers by Total Profit")

# Plotting the pie chart for top 10 customers
fig1, ax1 = plt.subplots(figsize=(3, 3))  # Adjusted figsize
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax1, colors=colors)
ax1.set_ylabel('')  # Remove the y-axis label
ax1.set_title('Top 10 Customers by Total Profit')

# Display the pie chart using Streamlit's st.pyplot() in the second column
with col2:
    st.pyplot(fig1)

# Second row: Product Selection Scatter Plot and Marketing Effectiveness Line Chart
col3, col4 = st.columns([2, 1])

# Display the topic of the second row
col3.markdown("### Product Selection: Sales vs. Profit")

# Selecting relevant columns for product analysis
product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

# Plotting the scatter plot for product selection
fig2, ax2 = plt.subplots(figsize=(3, 2))  # Adjusted figsize
ax2.scatter(product_data['Sales'], product_data['Profit'], alpha=0.5, c='lightgreen')
ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('P
