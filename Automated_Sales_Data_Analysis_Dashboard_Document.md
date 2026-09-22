# Project: Automated Sales Data Analysis Dashboard
--------------------------------

## Tech Stack
----------

Python (Core programming)

Pandas (Data loading & data cleaning)

Matplotlib (Visualization & reporting)

Schedule (Automation)

CSV (Data source)

## Project Summary
---------------

I developed an automated Sales Data Analysis Dashboard using Python, Pandas, Matplotlib, and Schedule. The system reads sales data from a CSV file, cleans the data, performs aggregation and analysis, and automatically generates daily visual reports.

### Data Extraction
----------------

Loaded sales data from a CSV file using Pandas `read_csv()`.

### Data Cleaning
----------------

Cleaned the sales dataset by:
- Removing duplicate records.
- Removing missing values.
- Converting the date column into proper datetime format.
- Removing records with negative sales values.

### Data Processing
----------------

Used Pandas `groupby()` and aggregation to analyze:
- Daily sales trends.
- Sales by category.
- Sales by region.
- Top 5 products by sales.

### Visualization
----------------

Created visual reports using Matplotlib:
- Line chart for daily sales trend.
- Bar chart for sales by category.
- Pie chart for sales by region.
- Bar chart for top 5 products.

### Automation
------------

Used the Schedule library to execute the dashboard job automatically at a configured time every day. The script also runs once immediately for testing before starting the scheduler.

### Output
---------

All generated charts are saved as PNG files inside the `reports` folder. Filenames include the current date so that reports can be maintained separately.

## Python Implementation
-----------------------

The implementation supplied for this project follows this flow:

Fetch Data → Clean Data → Create Charts → Run Job → Schedule Automation

### 1. Fetch Data
----------------

The `fetch_data()` function reads the sales CSV file and returns the data as a Pandas DataFrame.

```python
def fetch_data():
    data = pd.read_csv(r"D:\sales_data.csv")
    return data
```

### 2. Clean Data
----------------

The `clean_data(data)` function performs the main data-quality operations.

```python
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
```

### 3. Create Charts
-------------------

The `create_charts(data)` function creates the reports folder, gets today's date, performs the required aggregations, and saves the charts.

#### Daily Sales Trend

Daily sales are grouped by date and summed.

```python
daily_sales = (
    data.groupby("date")["sales"]
    .sum()
    .reset_index()
)
```

A line chart is then generated and saved as a PNG report.

#### Sales by Category

Sales are grouped by category and summed.

```python
category_sales = (
    data.groupby("category")["sales"]
    .sum()
)
```

A bar chart is generated to compare category-wise sales.

#### Sales by Region

Sales are grouped by region and summed.

```python
region_sales = (
    data.groupby("region")["sales"]
    .sum()
)
```

A pie chart is generated to show the regional distribution.

#### Top 5 Products

Sales are grouped by product, sorted in descending order, and the first five products are selected.

```python
top_products = (
    data.groupby("product")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
```

A bar chart is generated for the top products.

### 4. Main Job
-------------

The `job()` function controls the complete workflow.

```python
def job():

    data = fetch_data()

    data = clean_data(data)

    create_charts(data)
```

This makes the project easier to understand because each major task is separated into its own function.

### 5. Testing
-----------

The script runs the job once immediately before starting the scheduler.

```python
job()
```

This allows the dashboard generation process to be tested without waiting for the scheduled time.

### 6. Scheduled Automation
--------------------------

The Schedule library is used to execute the job every day at the configured time.

```python
schedule.every().day.at("16:02").do(job)
```

The scheduler continuously checks for pending jobs:

```python
while True:
    schedule.run_pending()
    time.sleep(60)
```

## Business Problem
#################

### Scenario
###########

A business receives sales data containing information such as date, product, category, region, and sales amount. The business needs a simple and repeatable way to monitor sales performance and identify useful patterns.

Manually preparing daily reports can take time and may introduce inconsistencies. A Python-based automated reporting system can perform the data preparation and generate visual reports on a scheduled basis.

### Specific Issues
################

- Difficulty in monitoring daily sales trends.
- Time required for manual data cleaning.
- Difficulty comparing sales across categories.
- Difficulty understanding regional sales distribution.
- Difficulty identifying top-performing products.
- Need for regular and consistent report generation.

## Proposed Solution
###################

To address these problems, an automated Sales Data Analysis Dashboard can be built using Python. The system reads the CSV data, cleans the dataset using Pandas, analyzes the sales information, generates charts using Matplotlib, and runs automatically using Schedule.

## Key Features of the Solution
#############################

### Automated Data Fetching
########################

The system automatically reads the sales dataset from the configured CSV file and loads it into a Pandas DataFrame.

### Data Quality and Cleaning
###########################

The system removes duplicate rows, removes missing values, converts dates into a proper datetime format, and filters out negative sales values.

### Sales Analysis
#################

The system provides analysis for:
- Daily sales performance.
- Category-wise sales.
- Region-wise sales.
- Top 5 products.

### Visualization
################

The system creates:
- Daily Sales Trend line chart.
- Sales by Category bar chart.
- Sales by Region pie chart.
- Top 5 Products bar chart.

### Automated Report Storage
###########################

The generated charts are saved automatically in a `reports` folder. The report filenames contain the current date.

### Scheduled Reporting
####################

The Schedule library runs the complete dashboard process every day at the configured time.

## Data Processing Flow
#####################

```text
CSV Sales Data
      ↓
Fetch Data using Pandas
      ↓
Data Cleaning
      ↓
Duplicate Removal
      ↓
Missing Value Removal
      ↓
Date Conversion
      ↓
Negative Sales Removal
      ↓
Pandas GroupBy & Aggregation
      ↓
Matplotlib Charts
      ↓
PNG Reports
      ↓
Scheduled Daily Execution
```

## Benefits of the Solution
#########################

### Time and Resource Efficiency
#############################

The automated process reduces the repetitive effort involved in preparing daily sales reports.

### Consistent Data Preparation
############################

The same cleaning steps are applied whenever the job runs, helping maintain a consistent reporting process.

### Faster Analysis
##################

The generated visualizations make it easier to review daily, category-wise, regional, and product-level sales information.

### Easy Report Access
####################

Reports are stored as PNG files in a dedicated `reports` folder, making them easy to access and share.

### Automated Reporting
####################

The scheduled execution removes the need to manually start the analysis every day after the system has been configured.

### Scalable Structure
####################

The project separates data fetching, cleaning, chart creation, and scheduling into different functions, making the script easier to maintain and extend.

## Project Output
################

The project generates the following report files:

- `daily_sales_YYYYMMDD.png`
- `sales_by_category_YYYYMMDD.png`
- `sales_by_region_YYYYMMDD.png`
- `top_products_YYYYMMDD.png`

## Resume Points
###############

- Developed an automated Sales Data Analysis Dashboard using Python, Pandas, Matplotlib, and Schedule.
- Implemented data cleaning techniques including duplicate removal, missing-value handling, date conversion, and negative-value filtering.
- Performed sales analysis using Pandas grouping and aggregation for daily trends, categories, regions, and top products.
- Created automated visual reports using Matplotlib and saved them as date-based PNG files.
- Implemented scheduled execution using Python's Schedule library for regular report generation.

## Important Note
################

The uploaded implementation uses a CSV file as the data source. It does not contain MySQL connectivity or Power BI implementation. Therefore, this document keeps the technology stack and project flow aligned with the supplied Python code rather than adding unsupported components.
