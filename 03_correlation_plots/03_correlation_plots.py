# PYTHON TIPS ----
# TIP 003 | Correlation Plots in Python ----
#
# 👉 For Weekly Python-Tips, Sign Up Here:
#    https://mailchi.mp/business-science/python_tips_newsletter

# LIBRARIES ----
import numpy as np
import pandas as pd

# DATASET ----
mpg_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
mpg_df

# 1.0 CORRELATION ----

mpg_df.corr()

# ?pd.DataFrame.corr

mpg_df.corr(method = 'spearman')

# 2.0 HEATMAP ----

df = mpg_df.corr()

# 2.1 Seaborn (Wide Format)
import seaborn as sea

sea.heatmap(
    data  = df, 
    annot = True
)

# 2.2 BONUS: Plotnine (Long Format)
import plotnine as p9
import plydata.cat_tools as cat

tidy_corr = mpg_df \
    .corr() \
    .melt(
        ignore_index=False,
    ) \
    .reset_index() \
    .set_axis(
        labels = ["var1", "var2", "value"],
        axis   = 1
    ) \
    .assign(lab_text = lambda x: np.round(x['value'], 2)) \
    .assign(
        var1 = lambda x: cat.cat_inorder(x['var1']),
        var2 = lambda x: 
            cat.cat_rev(
                cat.cat_inorder(x['var2'])
            )
    )

p9.ggplot(
    mapping = p9.aes("var1", "var2", fill = "value"),
    data    = tidy_corr
) + \
    p9.geom_tile() + \
    p9.geom_label(
        p9.aes(label = "lab_text"), 
        fill = "white",
        size = 8
    ) + \
    p9.scale_fill_distiller() + \
    p9.theme_minimal() + \
    p9.labs(
        title = "Vehicle Fuel Economy | Correlation Matrix",
        x = "", y = ""
    ) + \
    p9.theme(
        axis_text_x= p9.element_text(rotation=45, hjust = 1),
        figure_size=(8,6)
    )


# LEARNING PANDAS & PLOTNINE ----
# - Seaborn is great for making quick plots
# - Pandas + Plotnine for making professional report plots

# I TEACH PANDAS & PLOTNINE:
#   Python for Data Science Automation Course (Contains 5 hours of Pandas)
#   https://university.business-science.io/p/python-for-data-science-automation-ds4b-101p

