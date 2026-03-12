# Experiment 1: Data Wrangling Using Python

## Problem Statement

Perform Data Wrangling operations using Python on any open-source dataset.

The following tasks must be performed:

1. Import all the required Python libraries.
2. Locate an open-source dataset from the web (for example: Kaggle) and provide a clear description of the dataset along with its source URL.
3. Load the dataset into a Pandas DataFrame.
4. Perform Data Preprocessing:

   * Check for missing values using `isnull()`
   * Use `describe()` to obtain statistical information
   * Provide variable descriptions and types of variables
   * Check the dimensions of the DataFrame
5. Perform Data Formatting and Data Normalization:

   * Identify variable data types (character, numeric, integer, categorical, logical)
   * Convert variables to correct data types if required
6. Convert categorical variables into quantitative variables in Python.

---

# Dataset Information

Dataset Used: **Titanic Dataset**

Source:
https://www.kaggle.com/datasets/yasserh/titanic-dataset

### Dataset Description

The Titanic dataset contains information about passengers who were aboard the RMS Titanic ship.
The dataset includes passenger details such as age, gender, ticket class, fare, and survival status.

This dataset is widely used for learning **data preprocessing, data wrangling, and machine learning concepts**.
---

# Explanation of Steps

## 1. Import Required Libraries

Python libraries such as **Pandas, NumPy, Matplotlib, and Seaborn** are imported.
These libraries help in data manipulation, numerical computation, and visualization.

Example:

* `pandas` → used for data analysis and handling data tables
* `numpy` → used for numerical operations
---

## 2. Load the Dataset

The dataset is loaded using the `read_csv()` function from Pandas.

The dataset is stored in a **DataFrame**, which is a tabular structure containing rows and columns.

Example:

```python
df = pd.read_csv("titanic.csv")
```

---

## 3. Check Dataset Dimensions

The shape of the dataset is obtained using the `shape` function.

It returns:

* Number of rows
* Number of columns

Example:

```python
df.shape
```

---

## 4. Data Preprocessing

### Checking Missing Values

The `isnull()` function is used to detect missing values in the dataset.

Example:

```python
df.isnull().sum()
```

### Statistical Summary

The `describe()` function provides summary statistics such as:

* Mean
* Standard deviation
* Minimum value
* Maximum value
* Quartiles

Example:

```python
df.describe()
```

### Dataset Information

The `info()` function displays:

* Column names
* Data types
* Number of non-null values

Example:

```python
df.info()
```

---

## 5. Data Formatting and Data Normalization

### Checking Data Types

The data type of each column is checked using:

```python
df.dtypes
```

If variables are not in the correct format, they can be converted using `astype()`.

Example:

```python
df['Pclass'] = df['Pclass'].astype('category')
```

### Data Normalization

Normalization scales numerical values between **0 and 1**.

Formula:

```
(X − Min) / (Max − Min)
```

Example:

```python
df['Age_Normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
```

---

## 6. Convert Categorical Variables into Quantitative Variables

Machine learning algorithms require numerical input.
Therefore categorical variables such as **Sex** and **Embarked** are converted into numerical values using **One-Hot Encoding**.

Example:

```python
pd.get_dummies(df, columns=['Sex','Embarked'])
```

This creates new columns representing each category.

---

# Conclusion

In this experiment, we performed **Data Wrangling operations using Python** on an open-source dataset.

The following steps were successfully completed:

* Imported required Python libraries
* Loaded the dataset into a Pandas DataFrame
* Analyzed the structure and dimensions of the dataset
* Identified missing values and obtained statistical summaries
* Verified and corrected variable data types
* Normalized numerical variables
* Converted categorical variables into numerical variables

Data wrangling is an essential step in data analysis because it prepares raw data for further processing, visualization, and machine learning.
