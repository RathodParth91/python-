# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv("sales_data.csv", parse_dates=['Date'])
print("First few rows:\n", df.head(), "\n")

# Step 2: Add Revenue Column
df['Revenue'] = df['Quantity'] * df['Price']
print("With Revenue column:\n", df[['Product', 'Quantity', 'Price', 'Revenue']], "\n")

# Step 3: Total Revenue
total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue, "\n")

# Step 4: Revenue by Product
product_revenue = df.groupby('Product')['Revenue'].sum()
print("Revenue by Product:\n", product_revenue, "\n")

# Step 5: Revenue by Month
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("Revenue by Month:\n", monthly_revenue, "\n")

# Step 6: Revenue by Region
region_revenue = df.groupby('Region')['Revenue'].sum()
print("Revenue by Region:\n", region_revenue, "\n")

# Step 7: Visualization
# Revenue by Product
product_revenue.plot(kind='bar', title='Revenue by Product', ylabel='Revenue', color='skyblue')
plt.tight_layout()
plt.show()

# Monthly Revenue
monthly_revenue.plot(kind='line', title='Monthly Revenue Trend', marker='o', color='green')
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Revenue by Region
region_revenue.plot(kind='pie', title='Revenue by Region', autopct='%1.1f%%', figsize=(6,6))
plt.ylabel("")
plt.tight_layout()
plt.show()
