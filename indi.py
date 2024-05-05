import streamlit as st
import pandas as pd

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Display the bar chart title
st.title('Profit by Category')

# Display the bar chart with rotated x-axis labels for better readability
st.write('Bar Chart: Profit by Category')

# Plotting the bar chart using Streamlit's st.bar_chart()
st.bar_chart(profit_by_category.set_index('Category')['Profit'], use_container_width=True)  # Adjusts chart width


# Display the scatter plot title
st.title('Profit vs. Sales')

# Display the scatter plot
st.write('Line Chart: Profit vs. Sales')

# Plotting the scatter plot using Streamlit's st.line_chart()
st.line_chart(df[['Sales', 'Profit']])


#UNDERSTANDING ABOUT THE CUTOMER PREFERENCES
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have loaded your data into a DataFrame called df
# For example:
# df = pd.read_csv('path_to_your_csv_file.csv')

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

# Plotting the pie chart
top_customers_plot = top_customers['Total Profit'].plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=90)
top_customers_plot.set_ylabel('')  # Remove the y-axis label
top_customers_plot.set_title('Top 10 Customers by Total Profit')

plt.tight_layout()
plt.show()


