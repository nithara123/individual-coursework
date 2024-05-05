import streamlit as st
import pandas as pd

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Set up the layout of the dashboard
st.title('Sales and Profit Dashboard')

# Add a sidebar for user interaction
st.sidebar.title('Dashboard Options')
chart_type = st.sidebar.selectbox('Select Chart Type', ['Bar Chart', 'Scatter Plot'])

# Display the selected chart based on user's choice
if chart_type == 'Bar Chart':
    # Display the bar chart title
    st.subheader('Profit by Category')

    # Display the bar chart using Streamlit's st.bar_chart()
    st.bar_chart(profit_by_category.set_index('Category')['Profit'], use_container_width=True)  # Adjusts chart width

else:
    # Display the scatter plot title
    st.subheader('Profit vs. Sales')

    # Display the scatter plot using Streamlit's st.line_chart()
    st.line_chart(df[['Sales', 'Profit']])

# Add some descriptive text or explanations
st.write('This dashboard visualizes sales and profit data.')

# Optionally, you can add more interactivity or widgets to further enhance the dashboard



