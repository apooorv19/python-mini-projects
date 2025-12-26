# 📊 Python EDA Portfolio

This repository contains a set of **Exploratory Data Analysis (EDA)** projects built using Python.  
The projects focus on real-world datasets and show practical skills in **data cleaning, feature engineering, handling missing values, and basic data visualization**.

The purpose of this portfolio is to demonstrate how raw data is prepared and understood before applying machine learning models.

---

## 📁 Projects Included

### ✈️ Flight Price Prediction - EDA
**Main Focus**: Working with date, time, and string-based features.

**What was done**
- Extracted `Day`, `Month`, and `Year` from the journey date using pandas datetime functions.
- Cleaned arrival and departure time columns by removing extra date information using `split` and `lambda`.
- Combined training and test datasets to apply the same preprocessing steps to both.

---

### 🍔 Zomato Restaurant Data - EDA
**Main Focus**: Cleaning text data and analyzing restaurant details.

**What was done**
- Solved file reading issues by using `latin-1` encoding for text-heavy data.
- Checked and analyzed missing values across multiple columns such as `Cuisines`.
- Studied how ratings relate to cost range and types of cuisines.

---

### 🛍️ Black Friday Sales - EDA
**Main Focus**: Demographic data analysis and categorical variables.

**What was done**
- Converted age groups into numeric values for easier analysis.
- Encoded categorical variables like `City_Category` using One-Hot Encoding.
- Filled missing values in product-related columns and analyzed purchase behavior.

---

## 🛠️ Tools and Libraries

**Language**
- Python 3.x

**Libraries Used**
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🧠 Key Concepts Used

- **Data Cleaning**: Handling missing values and fixing inconsistent data.
- **Feature Engineering**: Creating new useful features from existing columns.
- **String Processing**: Using `split()`, lambda functions, and basic regex.
- **Categorical Encoding**: One-Hot Encoding and manual mapping.
- **Date and Time Handling**: Extracting useful parts from date columns.
- **Visualization**: Simple plots to understand distributions and relationships.

---

## 📂 Folder Structure

```bash
EDA/
├── Black Friday - EDA/
│   ├── bf_eda.ipynb
│   └── train.csv
├── Flight Prediction - EDA/
│   ├── fp_eda.ipynb
│   ├── Data_Train.xlsx
│   └── Test_set.xlsx
└── Zomato - EDA/
    ├── zomato_eda.ipynb
    └── zomato.csv
```

---

## 🙏 Acknowledgment

Special thanks to **Krish Naik** for the excellent educational content that helped in learning these EDA and Feature Engineering topics.
* **Reference Tutorial**: [Complete Feature Engineering- EDA- Krish Naik](https://youtu.be/fHFOANOHwh8?si=vyJtAEybWJJniFcm)
