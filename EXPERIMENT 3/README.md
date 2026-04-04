# Experiment 3 — Descriptive Statistics
### SPPU TE Computer Engineering | DSBDA Lab

## Problem Statement
Perform **Descriptive Statistics – Measures of Central Tendency and Variability** on open-source datasets.

1. Provide summary statistics (mean, median, min, max, std dev) for a dataset with numeric variables **grouped by a categorical variable**.
2. Display basic statistical details (percentile, mean, std dev, etc.) for each species in the **Iris dataset**.

---

## Datasets
| Dataset | Source | Used For |
|---------|--------|----------|
| `adult_data.csv` | [Kaggle – Salary Data](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data) | Part 1 – Grouped stats by Age |
| `iris.csv` | [Kaggle – Iris Dataset](https://www.kaggle.com/datasets/uciml/iris) | Part 2 – Species-wise statistics |

---

## Libraries Used
```python
import numpy as np
import pandas as pd
```

---

## What the Notebook Does

**Part 1 – Adult/Salary Dataset**
- Loads `adult_data.csv` and renames `Salary` → `income`
- Groups income by `Age` using `groupby().describe()`
- Creates a list of income values per age group using `.apply(list)`

**Part 2 – Iris Dataset**
- Loads `iris.csv` and runs `describe()` on the full dataset
- Filters each species and computes individual statistics
- Uses `np.percentile()` for 25th, 50th, 75th percentiles per species
- Uses `groupby('Species').describe()` and `.quantile()` for grouped output

---


## File Structure
```
Experiment_3/
├── Experiment_3.ipynb   # Main notebook with code + outputs
├── adult_data.csv       # Salary dataset
├── iris.csv             # Iris dataset
└── README.md            # This file
```
