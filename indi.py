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
selected_option = st.sidebar.selectbox("Select Visualization", ["Product Performance Insights", "Sales by Category", "Sales Over Time", "Sales Quantity Distribution"])

# Display selected visualization based on user choice
if selected_option == "Product Performance Insights":
    st.subheader('Product Performance Insights')
    try:
        # Assuming 'Sales', 'Quantity', 'Discount', 'Profit', and 'Shipping Cost' columns are available
        fig, axes = plt.subplots(1, 3, figsize=(20, 6))

        # Line graph - Sales Over Time
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        sales_over_time = df.groupby(pd.Grouper(key='Order Date', freq='M')).sum()['Sales']
        sns.lineplot(data=sales_over_time, ax=axes[0])
        axes[0].set_title('Sales Over Time')

        # Bubble chart - Sales vs. Profit vs. Quantity
        sns.scatterplot(data=df, x='Sales', y='Profit', size='Quantity', sizes=(20, 200), ax=axes[1])
        axes[1].set_title('Sales vs. Profit vs. Quantity')

        # Box plot - Sales Quantity Distribution
        sns.boxplot(data=df, y='Quantity', ax=axes[2])
        axes[2].set_title('Sales Quantity Distribution')

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error creating product performance insights: {e}")
