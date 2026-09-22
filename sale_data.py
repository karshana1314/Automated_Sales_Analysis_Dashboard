
import schedule
import time
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


# 1. Fetch data
def fetch_data():

    data = pd.read_csv(r"D:\sales_data.csv")

    return data


# 2. Clean data
def clean_data(data):

    # Remove duplicate records
    data = data.drop_duplicates()

    # Remove missing values
    data = data.dropna()

    # Convert date to proper date format
    data["date"] = pd.to_datetime(data["date"])

    # Remove negative sales
    data = data[data["sales"] >= 0]

    return data


# 3. Create charts
def create_charts(data):

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # Today's date
    today = datetime.now().strftime("%Y%m%d")


    # --------------------------
    # Daily Sales Trend
    # --------------------------

    daily_sales = (
        data.groupby("date")["sales"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        daily_sales["date"],
        daily_sales["sales"],
        marker="o"
    )

    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(True)

    plt.savefig(
        f"reports/daily_sales_{today}.png"
    )

    plt.close()


    # --------------------------
    # Sales by Category
    # --------------------------

    category_sales = (
        data.groupby("category")["sales"]
        .sum()
    )

    plt.figure(figsize=(6, 4))

    plt.bar(
        category_sales.index,
        category_sales.values
    )

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.savefig(
        f"reports/sales_by_category_{today}.png"
    )

    plt.close()


    # --------------------------
    # Sales by Region
    # --------------------------

    region_sales = (
        data.groupby("region")["sales"]
        .sum()
    )

    plt.figure(figsize=(6, 6))

    plt.pie(
        region_sales,
        labels=region_sales.index,
        startangle=90
    )

    plt.title("Sales by Region")

    plt.savefig(
        f"reports/sales_by_region_{today}.png"
    )

    plt.close()


    # --------------------------
    # Top 5 Products
    # --------------------------

    top_products = (
        data.groupby("product")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(6, 4))

    plt.bar(
        top_products.index,
        top_products.values
    )

    plt.title("Top 5 Products")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")

    plt.savefig(
        f"reports/top_products_{today}.png"
    )

    plt.close()


    print("All charts generated successfully!")
    print("Reports saved in reports folder")


# 4. Main Job
def job():

    print("\n==============================")
    print("Running Sales Dashboard")
    print("Time:", datetime.now())
    print("==============================")

    # Fetch data
    data = fetch_data()

    # Clean data
    data = clean_data(data)

    # Create charts
    create_charts(data)


# 5. Run once immediately for testing
job()


# 6. Schedule every day at 16:50
schedule.every().day.at("16:50").do(job)


print("\nScheduler started...")
print("Waiting for 16:50...")


# 7. Keep scheduler running
while True:

    schedule.run_pending()

    time.sleep(60)













