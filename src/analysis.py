import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
sales_df = pd.read_csv("data/sales_data.csv")
print("First 5 Rows")
print(sales_df.head())

print("\nDataset Shape")
print(sales_df.shape)

print("\nColumn Names")
print(sales_df.columns)

print("\nDataset Information")
sales_df.info()

print("\nMissing Values")
print(sales_df.isnull().sum())

print("\nDuplicate Records")
print(sales_df.duplicated().sum())

print("\nTotal Sales")
print(sales_df["Sales"].sum())

print("\nTotal Profit")
print(sales_df["Profit"].sum())

print("\nAverage Sales")
print(sales_df["Sales"].mean())

print("\nAverage Profit")
print(sales_df["Profit"].mean())

print("\nTop Selling Products")
top_products = sales_df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(top_products)

print("\nRegion-wise Sales")
region_sales = sales_df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

print("\nCategory-wise Profit")
category_profit = sales_df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print(category_profit)

# Convert Order_Date to datetime
sales_df["Order_Date"] = pd.to_datetime(sales_df["Order_Date"])

# Create Month Number
sales_df["Month_Number"] = sales_df["Order_Date"].dt.month

# Create Month Name
sales_df["Month"] = sales_df["Order_Date"].dt.month_name()

# Monthly Sales
print("\nMonthly Sales")

monthly_sales = (
    sales_df.groupby(["Month_Number", "Month"])["Sales"]
    .sum()
    .reset_index()
    .sort_values("Month_Number")
)

print(monthly_sales)
print(monthly_sales[["Month", "Sales"]])

# Monthly Sales Bar Chart

plt.figure(figsize=(10, 5))
plt.bar(monthly_sales["Month"], monthly_sales["Sales"])
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, _: f'{x/1000000:.0f}M')
)
plt.title("Monthly Sales", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=10)
plt.ylabel("Sales (Millions)", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig("output/monthly_sales_bar.png", dpi=300, bbox_inches="tight")
plt.show()

# Monthly Sales Line Chart

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=2
)
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, _: f'{x/1000000:.0f}M')
)
plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (Millions)", fontsize=6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.savefig("output/monthly_sales_line.png", dpi=300, bbox_inches="tight")
plt.show()

# Category-wise Sales Pie Chart

category_sales = (
    sales_df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(6, 6))
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Category-wise Sales Distribution", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("output/category_sales_pie.png", dpi=300, bbox_inches="tight")
plt.show()

# Top 10 Products by Sales

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.gca().xaxis.set_major_formatter(
    FuncFormatter(lambda x, _: f'{x/1000000:.1f}M')
)

plt.title("Top 10 Selling Products", fontsize=14, fontweight="bold")
plt.xlabel("Sales (Millions)")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/top10_products.png", dpi=300, bbox_inches="tight")
plt.show()


# Correlation Heatmap

correlation = sales_df[["Sales", "Quantity", "Profit", "Discount"]].corr()

print("\nCorrelation Matrix")
print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("output/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n====== BUSINESS INSIGHTS ======")

print(f"Highest Sales Region : {region_sales.idxmax()}")
print(f"Highest Profit Category : {category_profit.idxmax()}")
print(f"Best Selling Product : {top_products.idxmax()}")
print(f"Highest Sales Month : {monthly_sales.loc[monthly_sales['Sales'].idxmax(),'Month']}")
