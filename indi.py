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

# Define custom CSS styles for the dashboard
st.markdown(
    """
    <style>
    .header {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px 0;
        background-color: #f0f0f0;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .topic {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .frame {
        border: 1px solid #d3d3d3;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the header
st.markdown('<div class="header">Sales Analytics Dashboard</div>', unsafe_allow_html=True)

# First row: Profit vs. Sales Line Chart and Top 10 Customers by Total Profit Pie Chart
col1, col2 = st.columns([1, 1])

# Display the topic of the first row
col1.markdown('<div class="topic">Profit vs. Sales</div>', unsafe_allow_html=True)

# Plotting the scatter plot for Profit vs. Sales
with col1:
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.line_chart(df[['Sales', 'Profit']], width=400, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

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
col2.markdown('<div class="topic">Top 10 Customers by Total Profit</div>', unsafe_allow_html=True)

# Plotting the pie chart for top 10 customers
fig1, ax1 = plt.subplots(figsize=(6, 6))
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax1)
ax1.set_ylabel('')  # Remove the y-axis label
ax1.set_title('Top 10 Customers by Total Profit')

# Display the pie chart using Streamlit's st.pyplot() in the second column
with col2:
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

# Second row: Product Selection Scatter Plot and Marketing Effectiveness Line Chart
col3, col4 = st.columns([1, 1])

# Display the topic of the second row
col3.markdown('<div class="topic">Product Selection: Sales vs. Profit</div>', unsafe_allow_html=True)

# Selecting relevant columns for product analysis
product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

# Plotting the scatter plot for product selection
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.scatter(product_data['Sales'], product_data['Profit'], alpha=0.5)
ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('Product Selection: Sales vs. Profit')  # Naming the graph
ax2.grid(True)
plt.tight_layout()

# Displaying the scatter plot for product selection in the first column of the second row
with col3:
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

# Display the topic of the second row
col4.markdown('<div class="topic">Improvement in Marketing Effectiveness Over Time</div>', unsafe_allow_html=True)

# Group the data by Order Date and calculate the total profit
marketing_data = df.groupby('Order Date')['Profit'].sum().reset_index()

# Convert Order Date to datetime format
marketing_data['Order Date'] = pd.to_datetime(marketing_data['Order Date'])

# Sort data by Order Date
marketing_data = marketing_data.sort_values(by='Order Date')

# Create an interactive line chart for marketing effectiveness using Plotly
fig3 = px.line(marketing_data, x='Order Date', y='Profit', title='Improvement in Marketing Effectiveness Over Time')
fig3.update_traces(mode='markers+lines')  # Display both markers and lines
fig3.update_layout(xaxis_title='Order Date', yaxis_title='Total Profit')

# Calculate and add a trend line to show the overall trend
trendline = go.Scatter(x=marketing_data['Order Date'],
                       y=marketing_data['Profit'].rolling(window=7).mean(),
                       mode='lines',
                       name='Trend Line')
fig3.add_trace(trendline)

# Display the interactive line chart for marketing effectiveness using Plotly in the second column of the second row
with col4:
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Third row: Sales Quantity and Profit by Category Chart
col5, _ = st.columns([1, 1])

# Display the topic of the third row
col5.markdown('<div class="topic">Sales Quantity and Profit by Category</div>', unsafe_allow_html=True)

# Group the data by Category and calculate the total sales quantity and profit
sales_profit_by_category = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Sort categories by total profit in descending order
sorted_categories = sales_profit_by_category.sort_values(by='Profit', ascending=False)

# Plotting the chart for sales quantity and profit by category using Altair
chart = alt.Chart(sorted_categories).mark_bar().encode(
    x='Category',
    y='Profit',
    color=alt.condition(
        alt.datum.Profit > 0,
        alt.value('green'),  # Color for positive profits
        alt.value('red')  # Color for negative profits
    ),
    tooltip=['Category', 'Profit']
).properties(
    width=800,
    height=500,
    title='Sales Quantity and Profit by Category'
).interactive()

# Display the chart for sales quantity and profit by category using Streamlit in the third column of the third row
with col5:
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
