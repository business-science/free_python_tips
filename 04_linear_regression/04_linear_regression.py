# PYTHON TIPS ----
# TIP 004 | Linear Regression in Python with Scikit Learn ----
#
# 👉 For Weekly Python-Tips, Sign Up Here:
#    https://mailchi.mp/business-science/python_tips_newsletter

# LIBRARIES ----

import pandas as pd
import numpy as np
from sklearn import metrics

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# DATASET ----
mpg_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
mpg_df

# 1.0 LINEAR REGRESSION: MPG VS WEIGHT ----
#   - Ordinary Least Squares (OLS)
#     ?LinearRegression

df = mpg_df[['mpg', 'weight']]
df

y = mpg_df.mpg
X = mpg_df[['weight']]

# Fitting ----

model_lr = LinearRegression().fit(X, y)

model_lr


# Results ----

model_lr.coef_
model_lr.intercept_

# Predictions ----

model_lr.predict(df[['weight']])

# Variance Explained ----

r2_score(
    y_true = df.mpg, 
    y_pred = model_lr.predict(df[['weight']])
)


# 2.0 VISUALIZATION ----
#   - Plotnine: Custom Matplotlib Plots

from plotnine import ggplot, aes, geom_point, geom_line
from plotnine.themes import theme_minimal

df['fitted'] = model_lr.predict(df[['weight']])
df

ggplot(aes('weight', 'mpg'), df) \
    + geom_point(alpha = 0.5, color = "#2c3e50") \
    + geom_line(aes(y = 'fitted'), color = 'blue') \
    + theme_minimal()


# LEARNING PYTHON FOR DATA SCIENCE AUTOMATION ----
#   Pandas + Plotnine for making professional report plots
#   Python for Data Science Automation Course (Contains 5 hours of Pandas, 4 hours on Plotnine)
#   https://university.business-science.io/p/python-for-data-science-automation-ds4b-101p
