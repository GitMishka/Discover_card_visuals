import pandas as pd

# Replace 'file_path' with the path to your Excel file
file_path = r'C:\Users\Misha\Desktop\GitHub\Discover_card_visuals\Discover-Last12Months-20230507.xlsx'
# Read the Excel file
df = pd.read_excel(file_path, engine='openpyxl')

df['Trans. date'] = pd.to_datetime(df['Trans. date'])

import matplotlib.pyplot as plt
import seaborn as sns

monthly_spending = df.groupby(df['Trans. date'].dt.to_period('M')).sum()

# Plot the total spending per month
plt.figure(figsize=(12, 6))
sns.barplot(x=monthly_spending.index.astype(str), y=monthly_spending['Amount'])
plt.xlabel('Month')
plt.ylabel('Total Spending')
plt.title('Total Spending per Month')
plt.xticks(rotation=45)
plt.show()
category_spending = df.groupby('Category').sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=category_spending.index, y=category_spending['Amount'])
plt.xlabel('Category')
plt.ylabel('Total Spending')
plt.title('Total Spending by Category')
plt.xticks(rotation=45)
plt.show()

monthly_category_spending = df.groupby([df['Trans. date'].dt.to_period('M'), 'Category']).sum().reset_index()

monthly_category_spending['Trans. date'] = monthly_category_spending['Trans. date'].dt.to_timestamp()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_category_spending, x='Trans. date', y='Amount', hue='Category', marker='o')
plt.xlabel('Month')
plt.ylabel('Total Spending')
plt.title('Total Spending by Category over Time')
plt.xticks(rotation=45)
plt.show()
