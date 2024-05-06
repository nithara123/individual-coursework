import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Plotting the first chart: Profit vs. Sales
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.scatter(df['Sales'], df['Profit'], color='blue', alpha=0.5)
ax1.set_xlabel('Sales')
ax1.set_ylabel('Profit')
ax1.set_title('Profit vs. Sales')
ax1.grid(True)

# Display the first chart using Streamlit
st.title('Maximize Sales and Optimize Strategies')
st.pyplot(fig1)

# Plotting the second chart: Customer Preferences
customer_preferences = df.groupby(['Customer ID', 'Category'])['Profit'].sum().reset_index()
pivot_table = customer_preferences.pivot(index='Customer ID', columns='Category', values='Profit').fillna(0)
pivot_table['Total Profit'] = pivot_table.sum(axis=1)
sorted_customers = pivot_table.sort_values(by='Total Profit', ascending=False)
top_customers = sorted_customers.head(10)

fig2, ax2 = plt.subplots(figsize=(8, 8))
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax2)
ax2.set_ylabel('')
ax2.set_title('Top 10 Customers by Total Profit')

# Display the second chart using Streamlit
st.pyplot(fig2)

# Plotting the third chart: Product Selection
product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]
product_summary = product_data.groupby(['Product ID', 'Product Name']).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.scatter(product_summary['Sales'], product_summary['Profit'], alpha=0.5)
ax3.set_xlabel('Sales')
ax3.set_ylabel('Profit')
ax3.set_title('Product Selection: Sales vs. Profit')
ax3.grid(True)

# Display the third chart using Streamlit
st.pyplot(fig3)

# Plotting the fourth chart: Improvement in Marketing Effectiveness
marketing_data = df.groupby('Order Date')['Profit'].sum().reset_index()
marketing_data['Order Date'] = pd.to_datetime(marketing_data['Order Date'])
marketing_data = marketing_data.sort_values(by='Order Date')

fig4 = px.line(marketing_data, x='Order Date', y='Profit', title='Improvement in Marketing Effectiveness Over Time')
fig4.update_traces(mode='markers+lines')
fig4.update_layout(xaxis_title='Order Date', yaxis_title='Total Profit')
trendline = go.Scatter(x=marketing_data['Order Date'], y=marketing_data['Profit'].rolling(window=7).mean(), mode='lines', name='Trend Line')
fig4.add_trace(trendline)

# Display the fourth chart using Streamlit
st.plotly_chart(fig4)

# Plotting the fifth chart: Enhance Competitive Advantage
sales_profit_by_category = df.groupby('Category').agg({'Quantity': 'sum', 'Profit': 'sum'}).reset_index()
sorted_categories = sales_profit_by_category.sort_values(by='Profit', ascending=False)

chart = alt.Chart(sorted_categories).mark_bar().encode(
    x='Category',
    y='Profit',
    color=alt.condition(alt.datum.Profit > 0, alt.value('green'), alt.value('red')),
    tooltip=['Category', 'Profit']
).properties(width=600, height=400, title='Sales Quantity and Profit by Category').interactive()

# Display the fifth chart using Streamlit
st.altair_chart(chart)
