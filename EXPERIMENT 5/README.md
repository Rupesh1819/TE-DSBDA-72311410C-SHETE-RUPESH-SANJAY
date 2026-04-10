# Logistic Regression on Social Network Ads Dataset

## Overview

This project demonstrates how to implement Logistic Regression for classification using the Social_Network_Ads dataset. It also evaluates the model using a confusion matrix and key performance metrics.

---

## Objective

* Apply Logistic Regression for binary classification
* Evaluate model using:

  * Confusion Matrix
  * Accuracy
  * Error Rate
  * Precision
  * Recall

---

## Dataset

* File: `Social_Network_Ads.csv`
* Features:

  * Age
  * EstimatedSalary
* Target:

  * Purchased (0 or 1)

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## Implementation Steps

### 1. Import Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
```

---

### 2. Load Dataset

```python
dataset = pd.read_csv('Social_Network_Ads.csv')

```

---

### 3. Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split()
```

---

### 4. Feature Scaling

```python
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
```

---

### 5. Train Model

```python
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
```

---

### 6. Prediction

```python
y_pred = classifier.predict(X_test)
```

---

### 7. Confusion Matrix

```python
cm = confusion_matrix(y_test, y_pred)
```

---

### 8. Extract TP, FP, TN, FN

```python
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]
```

---

### 9. Performance Metrics

---

## Evaluation Metrics

| Metric     | Formula           |
| ---------- | ----------------- |
| Accuracy   | (TP + TN) / Total |
| Error Rate | (FP + FN) / Total |
| Precision  | TP / (TP + FP)    |
| Recall     | TP / (TP + FN)    |

---

## Sample Output

```
Confusion Matrix:
[[65  3]
 [ 8 24]]

Accuracy: 0.89
Error Rate: 0.11
Precision: 0.88
Recall: 0.75
```

---

## Conclusion

* Logistic Regression effectively classifies user purchase behavior
* Model performance is evaluated using confusion matrix and derived metrics
* The model achieves good accuracy on the dataset

---
