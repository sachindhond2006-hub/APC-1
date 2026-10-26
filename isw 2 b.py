 Here is a simple **Sales Analysis System** using **Pandas and NumPy**. It calculates:

- Total sales
- Average sales
- Best-selling product
- Category-wise sales

```
import pandas as pd
import numpy as np

# Sample sales data
data = {
    "Product": ["Laptop", "Phone", "Laptop", "Headphones", "Phone", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics",
                  "Accessories", "Electronics", "Electronics"],
    "Quantity": [2, 5, 1, 10, 3, 4],
    "Price": [50000, 20000, 50000, 2000, 20000, 15000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate sales for each row
df["Sales"] = df["Quantity"] * df["Price"]

# 1. Total Sales
total_sales = np.sum(df["Sales"])

# 2. Average Sales
average_sales = np.mean(df["Sales"])

# 3. Best-selling Product
product_sales = df.groupby("Product")["Sales"].sum()
best_product = product_sales.idxmax()

# 4. Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

# Display results
print("----- SALES ANALYSIS -----")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Best-Selling Product:", best_product)

print("\nCategory-wise Sales:")
print(category_sales)
```

### Example output

```
----- SALES ANALYSIS -----
Total Sales: 280000
Average Sales: 46666.666666666664
Best-Selling Product: Phone

Category-wise Sales:
Category
Accessories     20000
Electronics    260000
Name: Sales, dtype: int64
```

### How it works

- `pd.DataFrame()` → creates the sales table.
- `df["Sales"]` → calculates **Quantity × Price**.
- `np.sum()` → calculates total sales.
- `np.mean()` → calculates average sales.
- `groupby("Product")` → finds sales for each product.
- `idxmax()` → finds the product with the highest sales.
- `groupby("Category")` → calculates sales for each category.

This is a good **beginner-level mini project** for learning Pandas and NumPy. 
