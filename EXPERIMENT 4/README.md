#  SPPU DSBDA Lab Experiment – Data Analytics I

##  Linear Regression for Boston Housing Price Prediction

---

##  Problem Statement

Create a Linear Regression Model using Python/R to predict home prices using the Boston Housing Dataset. The dataset contains information about various houses in Boston with 506 samples and 14 feature variables.

 Objective: Predict the value of house prices (MEDV) using given features.

---

##  Dataset Details

* Dataset: Boston Housing Dataset (Kaggle)
* Total Records: 506
* Input Features: 13
* Output Variable: MEDV (Median house price in $1000s)

###  Feature Description

| Feature | Description                    |
| ------- | ------------------------------ |
| CRIM    | Crime rate                     |
| ZN      | Residential land zoning        |
| INDUS   | Industrial area proportion     |
| CHAS    | Charles River dummy variable   |
| NOX     | Nitric oxide concentration     |
| RM      | Average number of rooms        |
| AGE     | Age of property                |
| DIS     | Distance to employment centers |
| RAD     | Accessibility to highways      |
| TAX     | Property tax rate              |
| PTRATIO | Pupil-teacher ratio            |
| B       | Proportion of Black population |
| LSTAT   | % lower status population      |

---

## 🛠️ Tools & Technologies

* Python 
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn

---

##  Steps / Algorithm

1. Import required libraries
2. Load dataset
3. Perform data preprocessing

   * Handle missing values using SimpleImputer
4. Split dataset into training and testing sets
5. Train Linear Regression model
6. Predict house prices
7. Evaluate model using MSE, RMSE, R² Score

---

## 📈 Output

* MSE ≈ 25.01
* RMSE ≈ 5.00
* R² Score ≈ 0.66

 The model shows moderate accuracy.

---

---

##  Challenges

* Missing values in dataset
* Linear Regression cannot handle NaN directly
* Moderate accuracy due to linear assumptions

---


##  Conclusion

The Linear Regression model was successfully implemented to predict house prices. The model achieved moderate accuracy and demonstrates the relationship between housing features and price.

---

##  References

* Scikit-learn Documentation
* Kaggle Boston Housing Dataset

---
