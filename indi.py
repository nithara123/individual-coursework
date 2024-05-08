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
import seaborn as sns

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
selected_option = st.sidebar.selectbox("Product Performance", ["Line Graph - Sales vs. Profit", "Scatter Plot - Discount vs. Sales", "Bubble Chart - Sales vs. Discount vs. Profit"])

# Display selected visualization based on user choice
if selected_option == "Line Graph - Sales vs. Profit":
    st.subheader('Line Graph - Sales vs. Profit')
    fig_line, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Sales', y='Profit', data=df, ax=ax)
    ax.set_xlabel('Sales')
    ax.set_ylabel('Profit')
    ax.set_title('Line Graph - Sales vs. Profit')
    st.pyplot(fig_line)

elif selected_option == "Scatter Plot - Discount vs. Sales":
    st.subheader('Scatter Plot - Discount vs. Sales')
    fig_scatter, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Discount', y='Sales', data=df, alpha=0.5, ax=ax)
    ax.set_xlabel('Discount')
    ax.set_ylabel('Sales')
    ax.set_title('Scatter Plot - Discount vs. Sales')
    st.pyplot(fig_scatter)

elif selected_option == "Bubble Chart - Sales vs. Discount vs. Profit":
    st.subheader('Bubble Chart - Sales vs. Discount vs. Profit')
    fig_bubble, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Sales', y='Discount', size='Profit', data=df, alpha=0.5, ax=ax)
    ax.set_xlabel('Sales')
    ax.set_ylabel('Discount')
    ax.set_title('Bubble Chart - Sales vs. Discount vs. Profit')
    st.pyplot(fig_bubble)
