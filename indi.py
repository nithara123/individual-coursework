import streamlit as st
import pandas as pd

#MAXIMIZING THE PROFIT
# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Set up the layout of the dashboard
st.title('Sales and Profit Dashboard')

# Add a sidebar for user interaction
st.sidebar.title('Dashboard Options')
chart_type = st.sidebar.selectbox('Select Chart Type', ['Bar Chart', 'Scatter Plot'])

# Display the selected chart based on user's choice
if chart_type == 'Bar Chart':
    # Display the bar chart title
    st.subheader('Profit by Category')

    # Display the bar chart using Streamlit's st.bar_chart()
    st.bar_chart(profit_by_category.set_index('Category')['Profit'], use_container_width=True)  # Adjusts chart width

else:
    # Display the scatter plot title
    st.subheader('Profit vs. Sales')

    # Display the scatter plot using Streamlit's st.line_chart()
    st.line_chart(df[['Sales', 'Profit']])

# Add some descriptive text or explanations
st.write('This dashboard visualizes sales and profit data.')

# Optionally, you can add more interactivity or widgets to further enhance the dashboard

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


