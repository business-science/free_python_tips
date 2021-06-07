# PYTHON TIPS ----
# TIP 002 | Siuba: Dplyr for Python ----
#
# 👉 For Weekly Python-Tips, Sign Up Here:
#    https://mailchi.mp/business-science/python_tips_newsletter

# LIBRARIES ----
import numpy as np
import pandas as pd

from siuba import _
from siuba.dply.verbs import group_by, mutate, select, summarize, ungroup

# DATASET ----

mpg_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
mpg_df

# 1.0 GROUP BY + SUMMARIZE
# Goal: Mean and Standard Deviation of weight by engine size

weight_by_cyl_df = mpg_df >> \
    group_by("cylinders") >> \
    summarize(
        mean_weight = np.mean(_.weight),
        sd_weight   = np.std(_.weight)
    )

weight_by_cyl_df

# 2.0 GROUP BY + MUTATE
# Goal: De-mean the mpg by average of each cylinder

mpg_demeaned_by_cyl_df = mpg_df >> \
    select('name', 'cylinders', 'mpg') >> \
    group_by("cylinders") >> \
    mutate(
        mean_mpg = np.mean(_.mpg)
    ) >> \
    ungroup() >> \
    mutate(
        mpg_demeaned_by_cyl = _.mpg - _.mean_mpg
    )

mpg_demeaned_by_cyl_df

# 3.0 PANDAS 
mpg_demeaned_by_cyl_df[['name', 'cylinders', 'mpg_demeaned_by_cyl']] \
    .sort_values('mpg_demeaned_by_cyl', ascending = False) \
    .style \
    .background_gradient()

# LEARNING PANDAS ----
# - Siuba is great for when you are coming from R to Python (like me)
# - Teams use Pandas: 99% of data wranlging code is written with Pandas
# - Better Learn Pandas if you want to be part of the Team

# I TEACH PANDAS (FROM AN R-USERS PERSPECTIVE)!
# Python for Data Science Automation Course (Contains 5 hours of Pandas)
# https://university.business-science.io/p/python-for-data-science-automation-ds4b-101p
