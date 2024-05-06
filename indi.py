import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

st.set_page_config(layout="wide")

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
    .graph-frame {
        border: none;  /* Remove border */
        padding: 0;  /* Remove padding */
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="header">Analytics Dashboard</div>', unsafe_allow_html=True)

# First row
col1, col2 = st.columns([1, 1])

col1.markdown('<div class="topic">Profit vs. Sales</div>', unsafe_allow_html=True)

with col1:
    st.markdown('<div class="graph-frame">', unsafe_allow_html=True)
    st.line_chart(df[['Sales', 'Profit']], width=400, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

customer_preferences = df.groupby(['Customer ID', 'Category'])['Profit'].sum().reset_index()

pivot_table = customer_preferences.pivot(index='Customer ID', columns='Category', values='Profit').fillna(0)

pivot_table['Total Profit'] = pivot_table.sum(axis=1)

sorted_customers = pivot_table.sort_values(by='Total Profit', ascending=False)

top_customers = sorted_customers.head(10)

col2.markdown('<div class="topic">Top 10 Customers by Total Profit</div>', unsafe_allow_html=True)

fig1, ax1 = plt.subplots(figsize=(4, 4))  # Adjusted figsize
top_customers['Total Profit'].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax1)
ax1.set_ylabel('')  # Remove the y-axis label
ax1.set_title('Top 10 Customers by Total Profit')

with col2:
    st.markdown('<div class="graph-frame">', unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

# Second row
col3, col4 = st.columns([1, 1])

col3.markdown('<div class="topic">Product Selection: Sales vs. Profit</div>', unsafe_allow_html=True)

product_data = df[['Product ID', 'Product Name', 'Sales', 'Profit']]

fig2, ax2 = plt.subplots(figsize=(4, 3))  # Adjusted figsize
ax2.scatter(product_data['Sales'], product_data['Profit'], alpha=0.5)
ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('Product Selection: Sales vs. Profit')  # Naming the graph
ax2.grid(True)
plt.tight_layout()

with col3:
    st.markdown('<div class="graph-frame">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

col4.markdown('<div class="topic">Improvement in Marketing Effectiveness Over Time</div>', unsafe_allow_html=True)

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

# Third row
col5, _ = st.columns([1, 1])

col5.markdown('<div class="topic">Sales Quantity and Profit by Category</div>', unsafe_allow_html=True)

sales_profit_by_category = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

sorted_categories = sales_profit_by_category.sort_values(by='Profit', ascending=False)

chart = alt.Chart(sorted_categories).mark_bar().encode(
    x='Category',
    y='Profit',
    color=alt.condition(
        alt.datum.Profit > 0,
        alt.value('lightblue'),  
        alt.value('red')  
    ),
    tooltip=['Category', 'Profit']
).properties(
    width=400,  # Adjusted width
    height=300,  # Adjusted height
    title='Sales Quantity and Profit by Category'
).interactive()

with col5:
    st.altair_chart(chart, use_container_width=True)
