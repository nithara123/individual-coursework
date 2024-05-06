import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Display the scatter plot title
st.title('Profit vs. Sales')

# Plotting the scatter plot using Streamlit's st.line_chart()
st.line_chart(df[['Sales', 'Profit']], width=400, height=300)

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

# Plotting the pie chart for top 10 customers
fig1, ax1 = plt.subplots(figsize=(4, 4))
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax1)
ax1.set_ylabel('')  # Remove the y-axis label
ax1.set_title('Top 10 Customers by Total Profit')

# Display the pie chart using Streamlit's st.pyplot()
st.pyplot(fig1)

# Selecting relevant columns for product analysis
product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

# Grouping data by Product ID and calculating total sales quantity and profit
product_summary = product_data.groupby(['Product ID', 'Product Name']).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Plotting the scatter plot for product selection
fig2, ax2 = plt.subplots(figsize=(4, 3))
ax2.scatter(product_summary['Sales'], product_summary['Profit'], alpha=0.5)
ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('Product Selection: Sales vs. Profit')  # Naming the graph
ax2.grid(True)
plt.tight_layout()

# Displaying the scatter plot for product selection using Streamlit
st.pyplot(fig2)

# Group the data by Order Date and calculate the total profit
marketing_data = df.groupby('Order Date')['Profit'].sum().reset_index()

# Convert Order Date to datetime format
marketing_data['Order Date'] = pd.to_datetime(marketing_data['Order Date'])

# Sort data by Order Date
marketing_data = marketing_data.sort_values(by='Order Date')

# Create an interactive line chart for marketing effectiveness using Plotly
fig3 = px.line(marketing_data, x='Order Date', y='Profit', title='Marketing Effectiveness Over Time')
fig3.update_traces(mode='markers+lines')  # Display both markers and lines
fig3.update_layout(xaxis_title='Order Date', yaxis_title='Total Profit')

# Calculate and add a trend line to show the overall trend
trendline = go.Scatter(x=marketing_data['Order Date'],
                       y=marketing_data['Profit'].rolling(window=7).mean(),
                       mode='lines',
                       name='Trend Line')
fig3.add_trace(trendline)

# Display the interactive line chart for marketing effectiveness using Plotly
st.plotly_chart(fig3, use_container_width=True)

# Group the data by Category and calculate the total sales quantity and profit
sales_profit_by_category = df.groupby('Category').agg({'Quantity': 'sum'
