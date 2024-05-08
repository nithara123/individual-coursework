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
selected_option = st.sidebar.selectbox("Product Performance", ["Line Chart - Sales Quantity Over Time", "Discount vs Profit", "Bubble Chart - Profit vs Quantity"])

# Display selected visualization based on user choice
if selected_option == "Line Chart - Sales Quantity Over Time":
    st.subheader('Line Chart - Sales Quantity Over Time')
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        sales_quantity_over_time = df.groupby(pd.Grouper(key='Order Date', freq='M')).sum()['Quantity']
        fig_line, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=sales_quantity_over_time.index, y=sales_quantity_over_time.values, ax=ax)
        ax.set_xlabel('Order Date')
        ax.set_ylabel('Sales Quantity')
        ax.set_title('Line Chart - Sales Quantity Over Time')
        st.pyplot(fig_line)
    except Exception as e:
        st.error(f"Error creating line chart: {e}")

elif selected_option == "Discount vs Profit":
    st.subheader('Discount vs Profit')
    try:
        fig_scatter, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='Profit', y='Discount', data=df, alpha=0.5, ax=ax)
        ax.set_xlabel('Profit')
        ax.set_ylabel('Discount')
        ax.set_title('Scatterplot - Discount vs Profit')
        st.pyplot(fig_scatter)
    except Exception as e:
        st.error(f"Error creating scatterplot: {e}")

elif selected_option == "Bubble Chart - Profit vs Quantity":
    st.subheader('Bubble Chart - Profit vs Quantity')
    try:
        fig_bubble, ax = plt.subplots(figsize=(10, 8))
        sns.scatterplot(x='Profit', y='Quantity', size='Sales', data=df, alpha=0.5, ax=ax)
        ax.set_xlabel('Profit')
        ax.set_ylabel('Quantity')
        ax.set_title('Bubble Chart - Profit vs Quantity')
        st.pyplot(fig_bubble)
    except Exception as e:
        st.error(f"Error creating bubble chart: {e}")


#CUSTOMER ANALYSIS
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

# Sidebar menu options for customer analysis
selected_option = st.sidebar.selectbox("Customer Analysis", ["Pie Chart - Customer Segmentation", "Bar Graph - Sales by Customer Segment", "Line Graph - Sales Over Time by Customer Segment"])

# Display selected visualization based on user choice
if selected_option == "Pie Chart - Customer Segmentation":
    st.subheader('Pie Chart - Customer Segmentation')
    try:
        customer_segmentation = df['Segment'].value_counts()
        fig_pie, ax = plt.subplots()
        ax.pie(customer_segmentation, labels=customer_segmentation.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.title('Pie Chart - Customer Segmentation')
        st.pyplot(fig_pie)
    except Exception as e:
        st.error(f"Error creating pie chart: {e}")

elif selected_option == "Bar Graph - Sales by Customer Segment":
    st.subheader('Bar Graph - Sales by Customer Segment')
    try:
        sales_by_segment = df.groupby('Segment')['Sales'].sum()
        fig_bar, ax = plt.subplots(figsize=(8, 6))
        sales_by_segment.plot(kind='bar')
        plt.xlabel('Customer Segment')
        plt.ylabel('Sales')
        plt.title('Bar Graph - Sales by Customer Segment')
        st.pyplot(fig_bar)
    except Exception as e:
        st.error(f"Error creating bar graph: {e}")

elif selected_option == "Line Graph - Sales Over Time by Customer Segment":
    st.subheader('Line Graph - Sales Over Time by Customer Segment')
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        sales_over_time_segment = df.groupby(['Segment', pd.Grouper(key='Order Date', freq='M')]).sum()['Sales']
        fig_line, ax = plt.subplots(figsize=(10, 6))
        for segment, sales_data in sales_over_time_segment.groupby('Segment'):
            ax.plot(sales_data.index, sales_data.values, label=segment)
        plt.xlabel('Order Date')
        plt.ylabel('Sales')
        plt.title('Line Graph - Sales Over Time by Customer Segment')
        plt.legend()
        st.pyplot(fig_line)
    except Exception as e:
        st.error(f"Error creating line graph: {e}")
