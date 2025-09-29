import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv('Online Retail.csv', encoding='ISO-8859-1')

# Preview data
df.head()

# Check data types and nulls
df.info()

# Summary statics
df.describe()

# Count missing values
df.isnull().sum()

# Drop rows with missing CustomerID

df_clean = df.dropna(subset=['CustomerID'])

# Remove negative quantities
df_clean = df_clean[df_clean['Quantity'] > 0]

# Create a new column for TotalPrice
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']

# Convert invoiceDate to datetime
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'], dayfirst=True)

# Extract Year and Month
df_clean['InvoiceYear'] = df_clean['InvoiceDate'].dt.year
df_clean['InvoiceMonth'] = df_clean['InvoiceDate'].dt.month

# Visualisation
# Monthly
monthly_sales = df_clean.groupby(['InvoiceYear', 'InvoiceMonth'])['TotalPrice'].sum().reset_index()

plt.figure(figsize = (10,6))

sns.lineplot(data=monthly_sales, x='InvoiceMonth', y='TotalPrice', hue='InvoiceYear')
plt.title('Monthly Revenue Trend')

plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.show()

# Top 10 products by revenue

top_products = df_clean.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Products')
plt.show()

# Sales by country
country_sales = df_clean.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title('Top 10 Countries by Sales')
plt.xlabel('Revenue')
plt.ylabel('Country')
plt.show()