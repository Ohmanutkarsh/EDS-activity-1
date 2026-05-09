import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# Ensure 'Date' is in datetime format to extract the month easily
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Sales for each row (Quantity * Price)
df['Sales'] = df['Quantity'] * df['Price']

# Group by Month (formatted as YYYY-MM) and sum the sales
# We use .dt.to_period('M') to group by the specific month and year
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()

# Find the month with the highest total sales
best_month_period = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

# Convert the period back to string format for display (e.g., '2025-01')
best_month = str(best_month_period)

# Display the results as per the sample test case requirements
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
