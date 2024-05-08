import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS to style the sidebar
sidebar_style = """
    background-color: lightblue;
    padding: 10px;
    border-radius: 10px;
"""

# Apply the custom CSS to the sidebar
st.markdown(
    f"""
    <style>
    .sidebar .sidebar-content {{
        {sidebar_style}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load your dataset into a pandas DataFrame with error handling and proper encoding
try:
    df = pd.read_csv('https://github.com/nithara123/individual-coursework/raw/main/cleaned_dataset.csv', encoding='latin-1')
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Sidebar menu options
selected_option = st.sidebar.selectbox("Sales Overview", ["Sales by Category", "Sales Over Time", "Sales Quantity Distribution"])

# Display selected visualization based on user choice
if selected_option == "Sales by Category":
    st.subheader('Sales by Category')
    try:
        sales_by_category = df.groupby('Category')['Quantity'].sum()
        fig_bar = plt.figure(figsize=(8, 6))
        sales_by_category.plot(kind='bar')
        plt.xlabel('Category')
        plt.ylabel('Quantity')
        plt.xticks(rotation=45)
        plt.title('Bar Graph - Sales by Category')
        st.pyplot(fig_bar)
    except Exception as e:
        st.error(f"Error creating bar graph: {e}")
elif selected_option == "Sales Over Time":
    st.subheader('Sales Over Time')
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        sales_over_time = df.groupby(pd.Grouper(key='Order Date', freq='M')).sum()['Sales']
        fig_line = plt.figure(figsize=(10, 6))
        sales_over_time.plot(kind='line')
        plt.xlabel('Order Date')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.title('Line Graph - Sales Over Time')
        st.pyplot(fig_line)
    except Exception as e:
        st.error(f"Error creating line graph: {e}")
elif selected_option == "Sales Quantity Distribution":
    st.subheader('Sales Quantity Distribution')
    try:
        fig_hist = plt.figure(figsize=(8, 6))
        df['Quantity'].plot(kind='hist', bins=10)
        plt.xlabel('Quantity')
        plt.ylabel('Frequency')
        plt.title('Histogram - Sales Quantity Distribution')
        st.pyplot(fig_hist)
    except Exception as e:
        st.error(f"Error creating histogram: {e}")

#PRODUCT PERFOMANCE
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS to style the sidebar
sidebar_style = """
    background-color: lightblue;
    padding: 10px;
    border-radius: 10px;
"""

# Apply the custom CSS to the sidebar
st.markdown(
    f"""
    <style>
    .sidebar .sidebar-content {{
        {sidebar_style}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load your dataset into a pandas DataFrame with error handling and proper encoding
try:
    df = pd.read_csv('https://github.com/nithara123/individual-coursework/raw/main/cleaned_dataset.csv', encoding='latin-1')
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Line graph - Sales Quantity Over Time
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_quantity_over_time = df.groupby(pd.Grouper(key='Order Date', freq='M')).sum()['Sales Quantity']
fig_line = plt.figure(figsize=(10, 6))
plt.plot(sales_quantity_over_time.index, sales_quantity_over_time.values)
plt.xlabel('Order Date')
plt.ylabel('Sales Quantity')
plt.title('Line Graph - Sales Quantity Over Time')
st.pyplot(fig_line)

# Scatter plot - Sales Quantity vs. Profit
fig_scatter = plt.figure(figsize=(8, 6))
plt.scatter(df['Profit'], df['Sales Quantity'], alpha=0.5)
plt.xlabel('Profit')
plt.ylabel('Sales Quantity')
plt.title('Scatter Plot - Sales Quantity vs. Profit')
st.pyplot(fig_scatter)

# Bubble chart - Sales Quantity vs. Discount vs. Profit
fig_bubble, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(df['Discount'], df['Profit'], s=df['Sales Quantity']*10, alpha=0.5)
ax.set_xlabel('Discount')
ax.set_ylabel('Profit')
ax.set_title('Bubble Chart - Sales Quantity vs. Discount vs. Profit')
st.pyplot(fig_bubble)
