# PYTHON TIPS ----
# TIP 005 | Sweetviz ----
#
# 👉 For Weekly Python-Tips, Sign Up Here:
#    https://learn.business-science.io/python-tips-newsletter

# LIBRARIES ----

# GitHub: https://github.com/fbdesignpro/sweetviz

# pip install sweetviz

import pandas as pd
import sweetviz as sv

import plotnine as pn

# DATASET ----

mpg_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")

mpg_df

# SWEETVIZ ----

report = sv.analyze(
    mpg_df,
    target_feat='mpg'
)

report.show_html(
    filepath = "05_sweetviz/report.html"
)

# PLOTNINE -----
# - Learn plotnine in DS4B 101-P

pn.ggplot(
    pn.aes(
        'horsepower', 'acceleration', 
        color = 'mpg',
        size  = 'mpg'
    ),
    data = mpg_df
) + \
    pn.geom_point(alpha = 0.5) + \
    pn.geom_smooth(
        method = "lowess", 
        span   = 0.3,
        color  = 'blue'
    ) + \
    pn.guides(size = False) + \
    pn.theme_classic()
    

# LEARNING MORE:
# Python for Data Science Automation Course: 
# https://university.business-science.io/p/python-for-data-science-automation-ds4b-101p