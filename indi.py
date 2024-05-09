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


try:
    df = pd.read_csv('https://github.com/nithara123/individual-coursework/raw/main/cleaned_dataset.csv', encoding='latin-1')
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Sidebar menu options
selected_option = st.sidebar.selectbox("Sales Overview", ["Sales by Category", "Sales Over Time", "Sales Quantity Distribution"])

# Display selected visualization 
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

# PRODUCT PERFORMANCE
selected_option_perf = st.sidebar.selectbox("Product Performance", ["Line Chart - Sales Quantity Over Time", "Discount vs Profit", "Bubble Chart - Profit vs Quantity"])

if selected_option_perf == "Line Chart - Sales Quantity Over Time":
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

elif selected_option_perf == "Discount vs Profit":
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

elif selected_option_perf == "Bubble Chart - Profit vs Quantity":
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

# GEOGRAPHICAL INSIGHTS
selected_option_geo = st.sidebar.selectbox("Geographical Insights", ["Bar Graph - Sales by Region", "Heatmap - Sales by Category and Region"])

if selected_option_geo == "Bar Graph - Sales by Region":
    st.subheader('Bar Graph - Sales by Region')
    try:
        sales_by_region = df.groupby('Region')['Sales'].sum()
        fig_bar = plt.figure(figsize=(10, 6))
        sales_by_region.plot(kind='bar')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.title('Bar Graph - Sales by Region')
        st.pyplot(fig_bar)
    except Exception as e:
        st.error(f"Error creating bar graph: {e}")

elif selected_option_geo == "Heatmap - Sales by Category and Region":
    st.subheader('Heatmap - Sales by Category and Region')
    try:
        sales_by_category_and_region = df.pivot_table(index='Category', columns='Region', values='Sales', aggfunc='sum')
        fig_heatmap = plt.figure(figsize=(10, 6))
        sns.heatmap(sales_by_category_and_region, cmap='YlGnBu', annot=True, fmt='.1f')
        plt.title('Heatmap - Sales by Category and Region')
        st.pyplot(fig_heatmap)
    except Exception as e:
        st.error(f"Error creating heatmap: {e}")

# CUSTOMER ANALYSIS
selected_option_cust = st.sidebar.selectbox("Customer Analysis", ["Pie Chart - Customer Segmentation", "Bar Graph - Sales by Customer Segment"])

if selected_option_cust == "Pie Chart - Customer Segmentation":
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

elif selected_option_cust == "Bar Graph - Sales by Customer Segment":
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

# Filter by Category and Region
st.sidebar.header("Filter by Category and Region")
selected_category = st.sidebar.selectbox("Select Category", df['Category'].unique())
selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())

# Apply filters to the dataframe
filtered_df = df[(df['Category'] == selected_category) & (df['Region'] == selected_region)]

# Display the filtered data
st.write("Filtered Data:")
st.write(filtered_df)
