# individual-coursework
Data visualizing
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

# Load the CSV file into a DataFrame with 'latin1' encoding
df = pd.read_csv('C:/Users/Admin/Downloads/Global Superstore lite (1).csv', encoding='latin1')

# Calculate profit by category
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Plotting the bar chart
plt.bar(profit_by_category['Category'], profit_by_category['Profit'])
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Profit by Category')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


plt.scatter(df['Sales'], df['Profit'])
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Profit vs. Sales')
plt.show()

