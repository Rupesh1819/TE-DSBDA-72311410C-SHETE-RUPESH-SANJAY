# Experiment 2: Data Cleaning and Transformation Using Python

## Problem Statement
**Data Wrangling-II**, Create an “Academic performance” dataset of students and perform the following operations using Python.
1. Scan all variables for missing values and inconsistencies. If there are missing values and/or inconsistencies, use any of the suitable techniques to deal with them.
2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques to deal with them.
3. Apply data transformations on at least one of the variables. The purpose of this transformation should be one of the following reasons:
 to change the scale for better understanding of the variable, to convert a non-linear relation into a linear one,
 or to decrease the skewness and convert the distribution into a normal distribution. Reason and document your approach properly.
---

## Dataset Information

Dataset: Students Performance in Exams  
Source: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams  

---

## Steps Performed

### 1. Import Libraries
- pandas
- numpy
- matplotlib
- seaborn

### 2. Load Dataset
```python
df = pd.read_csv("StudentsPerformance.csv")
```

### 3. Data Understanding
```python
df.info()
df.describe()
df.shape
```

### 4. Handling Missing Values
```python
df.isnull().sum()
df.fillna(df.mean(), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)
```

### 5. Outlier Detection (IQR Method)
```python
Q1 = df['math score'].quantile(0.25)
Q3 = df['math score'].quantile(0.75)
IQR = Q3 - Q1
```

### 6. Removing Outliers
```python
df = df[(df['math score'] >= Q1 - 1.5*IQR) & 
        (df['math score'] <= Q3 + 1.5*IQR)]
```

### 7. Data Transformation (Log)
```python
df['math_score_log'] = np.log1p(df['math score'])
```

---

## Conclusion

- Missing values handled using mean/mode  
- Outliers removed using IQR  
- Log transformation applied to reduce skewness  

