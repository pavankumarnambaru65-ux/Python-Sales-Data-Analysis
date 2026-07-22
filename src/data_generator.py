import pandas as pd
import random
from datetime import datetime, timedelta

products = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
    "Tablet", "Headphones", "Webcam", "SSD", "RAM"
]

categories = [
    "Electronics", "Accessories", "Storage"
]

regions = [
    "Hyderabad", "Vijayawada", "Visakhapatnam", "Tirupathi", "Guntur"
]

payment_methods = [
    "Credit Card", "Debit Card", "UPI", "Net Banking", "Cash"
]

customers = [
    "Pavan", "Rahul", "Akhil", "Sai", "Kiran",
    "Priya", "Anjali", "Sneha", "Ravi", "Arjun",
    "Neha", "Vijay", "Suresh", "Keerthi", "Nikhil",
    "Harsha", "Divya", "Naveen", "Varun", "Swathi"
]

def generate_sales_data(num_records):
    sales_data = []
    start_date = datetime(2025, 1, 1)

    for i in range(num_records):
        order_id = 1001 + i
        order_date = start_date + timedelta(days=random.randint(0, 364))
        customer = random.choice(customers)
        product = random.choice(products)
        category = random.choice(categories)
        region = random.choice(regions)
        payment_method = random.choice(payment_methods)
        quantity = random.randint(1, 5)
        unit_price = random.randint(500, 50000)
        discount = random.randint(0, 30)

        sales = quantity * unit_price
        sales_after_discount = sales - (sales * discount / 100)
        profit = sales_after_discount * random.uniform(0.10, 0.30)
        sales_data.append({
            "Order_ID": order_id,
            "Order_Date": order_date.strftime("%Y-%m-%d"),
            "Customer_Name": customer,
            "Product": product,
            "Category": category,
            "Region": region,
            "Quantity": quantity,
            "Unit_Price": unit_price,
            "Discount": discount,
            "Sales": round(sales_after_discount, 2),
            "Profit": round(profit, 2),
            "Payment_Method": payment_method
        })
        df = pd.DataFrame(sales_data)
    return df
sales_df = generate_sales_data(10000)

sales_df.to_csv("data/sales_data.csv", index=False)

print("Sales dataset generated successfully!")
print(sales_df.head())