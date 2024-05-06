import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')
# Layout
st.set_page_config(layout="wide")

# First row: Profit vs. Sales Line Chart and Top 10 Customers by Total Profit Pie Chart
col1, col2 = st.columns([2, 1])

with col1:
    st.title('Profit vs. Sales')
    st.line_chart(df[['Sales', 'Profit']], width=600, height=400)

customer_preferences = df.groupby(['Customer ID', 'Category'])['Profit'].sum().reset_index()

pivot_table = customer_preferences.pivot(index='Customer ID', columns='Category', values='Profit').fillna(0)

pivot_table['Total Profit'] = pivot_table.sum(axis=1)

sorted_customers = pivot_table.sort_values(by='Total Profit', ascending=False)

top_customers = sorted_customers.head(10)

fig1, ax1 = plt.subplots(figsize=(6, 6))
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax1)
ax1.set_ylabel('')  # Remove the y-axis label
ax1.set_title('Top 10 Customers by Total Profit')

with col2:
    st.pyplot(fig1)

# Second row: Product Selection Scatter Plot and Marketing Effectiveness Line Chart
col3, col4 = st.columns([2, 1])

product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.scatter(product_data['Sales'], product_data['Profit'], alpha=0.5)
ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('Product Selection: Sales vs. Profit')  
ax2.grid(True)
plt.tight_layout()

with col3:
    st.pyplot(fig2)

marketing_data = df.groupby('Order Date')['Profit'].sum().reset_index()

marketing_data['Order Date'] = pd.to_datetime(marketing_data['Order Date'])

marketing_data = marketing_data.sort_values(by='Order Date')

fig3 = px.line(marketing_data, x='Order Date', y='Profit', title='Improvement in Marketing Effectiveness Over Time')
fig3.update_traces(mode='markers+lines')  # Display both markers and lines
fig3.update_layout(xaxis_title='Order Date', yaxis_title='Total Profit')

trendline = go.Scatter(x=marketing_data['Order Date'],
                       y=marketing_data['Profit'].rolling(window=7).mean(),
                       mode='lines',
                       name='Trend Line')
fig3.add_trace(trendline)

with col4:
    st.plotly_chart(fig3, use_container_width=True)

# Third row: Sales Quantity and Profit by Category Chart
col5, _ = st.columns([2, 1])

sales_profit_by_category = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

sorted_categories = sales_profit_by_category.sort_values(by='Profit', ascending=False)

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
    width=600,
    height=400,
    title='Sales Quantity and Profit by Category'
).interactive()

with col5:
    st.altair_chart(chart, use_container_width=True)

