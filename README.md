# Automated Sales Dashboard

## 📌 Project Overview

The **Automated Sales Dashboard** is a data analytics project that extracts sales data from a MySQL database, cleans and analyzes the data using Python, and automatically generates sales reports as charts.

The project helps analyze sales performance across different **dates, products, categories, and regions** and reduces the need for manual report generation.

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **SQL**
* **Pandas**
* **Matplotlib**
* **Schedule**

## 🔄 Project Workflow

```text
MySQL Database
      ↓
     SQL
      ↓
Python + Pandas
      ↓
Data Cleaning
      ↓
Data Analysis
      ↓
Matplotlib
      ↓
Automated Reports
```

## 📊 Key Analysis

The project generates reports for:

* Daily Sales
* Sales by Category
* Sales by Region
* Top-Selling Products

## 🧹 Data Cleaning

The data processing pipeline performs basic data-quality checks such as:

* Removing duplicate records
* Handling missing values
* Converting date columns into the correct format
* Checking sales values
* Checking data types

## ⚙️ Automation

The **Schedule** library is used to automate the report-generation process.

The system can run the dashboard automatically at a scheduled time and save the generated charts inside the `reports/` folder.

## 📁 Project Structure

```text
Automated-Sales-Dashboard/
│
├── sale_data.py
├── sales_table.sql
├── reports/
│   ├── daily_sales.png
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   └── top_products.png
│
└── README.md
```

## 🗄️ Database

The project uses **MySQL** to store sales data.

Database:

```text
yourdatabase
```

Table:

```text
sales_table
```

The sales table contains information related to:

* Date
* Product
* Category
* Region
* Sales

## 🚀 How to Run

### 1. Install required libraries

```bash
pip install pandas matplotlib mysql-connector-python schedule
```

### 2. Set up MySQL

Create the database and import the SQL file into MySQL Workbench.

### 3. Configure the Python file

Update the MySQL connection details in `sale_data.py` with your own:

```text
host
user
password
database
```

### 4. Run the project

```bash
python sale_data.py
```

The generated reports will be saved in the `reports/` folder.

## 🎯 Project Outcome

This project demonstrates practical knowledge of:

* SQL data extraction
* MySQL database handling
* Python programming
* Data cleaning
* Exploratory data analysis
* Data visualization
* Report automation

## 👩‍💻 Author

**Karshana**
