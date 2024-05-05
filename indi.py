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
import streamlit as st
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

# Plotting the pie chart and assigning it to a variable
fig, ax = plt.subplots(figsize=(8, 8))
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
ax.set_ylabel('')  # Remove the y-axis label
ax.set_title('Top 10 Customers by Total Profit')

# Display the pie chart using Streamlit's st.pyplot()
st.pyplot(fig)


#OPTIMIZE PRODUCT SELECTION
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have loaded your data into a DataFrame called df
# For example:
# df = pd.read_csv('path_to_your_csv_file.csv')

# Selecting relevant columns for analysis
product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

# Grouping data by Product ID and calculating total sales quantity and profit
product_summary = product_data.groupby(['Product ID', 'Product Name']).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Plotting the scatter plot to visualize product selection
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(product_summary['Sales'], product_summary['Profit'], alpha=0.5)
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
ax.set_title('Product Selection: Sales vs. Profit')  # Naming the graph
ax.grid(True)
plt.tight_layout()

# Displaying the named figure in Streamlit
st.title('Product Selection: Sales vs. Profit')  # Display figure title in Streamlit
st.pyplot(fig)  # Display the figure in Streamlit



#IMPROVE MARKETING EFFECTIVENESS
import pandas as pd
import plotly.express as px
import streamlit as st

# Assuming you have loaded your data into a DataFrame called df
# For example:
# df = pd.read_csv('path_to_your_csv_file.csv')

# Group the data by Order Date and calculate the total profit
marketing_data = df.groupby('Order Date')['Profit'].sum().reset_index()

# Convert Order Date to datetime format
marketing_data['Order Date'] = pd.to_datetime(marketing_data['Order Date'])

# Sort data by Order Date
marketing_data = marketing_data.sort_values(by='Order Date')

# Create an interactive line chart using Plotly
fig = px.line(marketing_data, x='Order Date', y='Profit', title='Improvement in Marketing Effectiveness Over Time')
fig.update_traces(mode='markers+lines')  # Display both markers and lines
fig.update_layout(xaxis_title='Order Date', yaxis_title='Total Profit')

# Calculate and add a trend line to show the overall trend
fig.add_trace(px.get_trendline_results(fig).iloc[:, 1])

# Display the figure with a title using Streamlit
st.title('Improvement in Marketing Effectiveness Over Time')
st.plotly_chart(fig)

