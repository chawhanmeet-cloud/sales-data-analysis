import pandas as pd

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

total_revenue = df["Revenue"].sum()

product_revenue = df.groupby("Product")["Revenue"].sum()

region_revenue = df.groupby("Region")["Revenue"].sum()

product_quantity = df.groupby("Product")["Quantity"].sum()

avg_price = df.groupby("Product")["Unit_Price"].mean()

monthly_revenue = df.groupby(df["Date"].dt.month)["Revenue"].sum()

highest_month = monthly_revenue.idxmax()
highest_revenue = monthly_revenue.max()

number_of_orders = len(df)
avg_order_value = total_revenue / number_of_orders

max_revenue = df["Revenue"].max()

customer_highest_revenue = df.groupby("Customer")["Revenue"].sum() 

category_revenue = df.groupby("Category")["Revenue"].sum()

highest_category = category_revenue.idxmax()
highest_category_revenue = category_revenue.max()

print("Total Revenue:", total_revenue)

print("Number of Orders:", number_of_orders)

print("Average Order Value:", avg_order_value)

print("Highest Order Revenue:", max_revenue)

print("Highest Revenue Category:", highest_category)

print("Highest Category Revenue:", highest_category_revenue)

print("Highest Revenue Month:", highest_month)

print("Highest Month Revenue:", highest_revenue)

print("Highest Revenue Customer:", customer_highest_revenue.idxmax())