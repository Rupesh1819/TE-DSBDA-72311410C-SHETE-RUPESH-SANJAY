# Data Visualization I - Titanic Dataset (DSBDA Experiment)

## Problem Statement 
**Data Visualization I**
1. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information
about the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library to
see if we can find any patterns in the data.
2. Write a code to check how the price of the ticket (column name: 'fare') for each passenger
is distributed by plotting a histogram.

##  Overview
This project demonstrates **Data Visualization techniques** using the inbuilt Titanic dataset from the Seaborn library. The goal is to identify patterns in passenger data and analyze fare distribution.

---

##  Objective
- Explore Titanic dataset using Seaborn
- Identify patterns in data (survival, gender, class, etc.)
- Visualize fare distribution using histogram

---

##  Theory

### 1. Data Visualization
Data Visualization is the graphical representation of data to understand patterns, trends, and relationships.

### 2. Seaborn Library
Seaborn is a Python visualization library based on Matplotlib. It provides attractive and informative statistical graphics.

### 3. Histogram
A histogram is used to visualize the distribution of numerical data by dividing it into bins.

---

##  Technologies Used
- Python
- Pandas
- Seaborn
- Matplotlib

---

##  Dataset Information
- Dataset: Titanic (inbuilt in Seaborn)
- Rows: 891
- Contains passenger details such as:
  - Age
  - Gender
  - Passenger Class
  - Fare
  - Survival status

---

##  Visualizations Performed

### 1. Survival Count Plot
Shows number of passengers who survived vs not survived.

### 2. Gender vs Survival
Shows survival distribution based on gender.

### 3. Passenger Class vs Survival
Shows how class affects survival probability.

### 4. Age Distribution
Histogram showing distribution of passenger ages.

### 5. Fare Distribution (Histogram)
Displays how ticket prices are distributed among passengers.

---

##  How to Run
1. Install required libraries:
   ```bash
   pip install seaborn matplotlib pandas
   ```
2. Open Jupyter Notebook or Google Colab
3. Run the Python code

---

##  Observations
- Females had higher survival rate than males
- First-class passengers had better survival chances
- Most passengers were aged between 20–40
- Fare distribution is right-skewed (few high values, many low values)

---

##  Conclusion
Data visualization helps in extracting meaningful insights from datasets. Using Seaborn, we identified survival patterns and analyzed fare distribution effectively.

---

## 📎 Notes
This experiment is part of the **DSBDA (Data Science and Big Data Analytics)** practical curriculum.
