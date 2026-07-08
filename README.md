# 🚀 Retail Sales ETL Pipeline using PySpark & Databricks

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using **PySpark** on **Databricks**. The pipeline processes multiple retail datasets, performs data cleaning and transformations, and loads the final dataset into a **MySQL Cloud Database (Aiven)** for analysis.

---

## 🏗️ Project Architecture

```
CSV Files
     │
     ▼
Databricks (PySpark)
     │
     ▼
Data Cleaning
     │
     ▼
Data Transformation
     │
     ▼
Aiven MySQL (Cloud)
     │
     ▼
SQL Analysis (DataGrip)
```

---

## 📂 Dataset

This project uses four datasets:

- Orders
- Customers
- Products
- Stores

---

## ⚙️ ETL Workflow

### 🔹 Extract
- Loaded multiple CSV files into PySpark DataFrames.

### 🔹 Transform
- Removed duplicate records.
- Handled missing values.
- Joined Orders, Customers, Products, and Stores datasets.
- Calculated **Total Amount**.
- Calculated **Final Amount** after discount.
- Extracted:
  - Order Year
  - Order Month
  - Order Day

### 🔹 Load
- Loaded the transformed data into a **MySQL Cloud Database (Aiven)** using Databricks.

---

## 🛠️ Tech Stack

- Python
- PySpark
- Databricks
- SQL
- MySQL
- Aiven Cloud
- DataGrip

---

## 📊 Features

- Data Cleaning
- Null Value Handling
- Duplicate Removal
- Multi-table Joins
- Business Transformations
- Date Feature Engineering
- Cloud Database Integration
- SQL-Based Data Validation

---

## 📁 Project Structure

```
Retail-Sales-ETL-Pipeline/
│
├── notebooks/
├── data/
├── screenshots/
├── sql/
├── README.md
└── requirements.txt
```

---

## 📸 Screenshots

Project screenshots are available in the **screenshots/** folder.

---

## 🚀 Future Improvements

- Apache Airflow
- Apache Kafka
- AWS S3
- Data Warehouse
- Snowflake
- Delta Lake

---

## 👨‍💻 Author

**Devanshu Jangid**

- LinkedIn: https://www.linkedin.com/in/devanshu-jangid-6066b4321
- GitHub: https://github.com/DEVANSHU362

---

⭐ If you found this project useful, consider giving it a star!
