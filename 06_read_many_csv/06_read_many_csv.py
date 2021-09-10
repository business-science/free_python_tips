# PYTHON TIPS ----
# TIP 006 | Reading Many CSV Files ----
#
# 👉 For Weekly Python-Tips, Sign Up Here:
#    https://mailchi.mp/business-science/python_tips_newsletter

# LIBRARIES ----

import pandas as pd
import glob

# FILE PATHS WITH GLOB ----

path = '06_read_csv_map/car_data/'
all_files = glob.glob(path + "/*.csv")

all_files

# METHOD 1: FOR-LOOP ---
# - 99% of Python People do some variation of this... 
# - But it's not concise and slower due to append

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

li

df = pd.concat(li, axis=0, ignore_index=True)
df

# METHOD 2: MAP ----
# - Benefits: Don't need to make for-loop / More concise / No list construction / Slightly Faster

li_mapper = map(lambda filename: pd.read_csv(filename, index_col=None, header=0), all_files)

li_2 = list(li_mapper)

df = pd.concat(li_2, axis=0, ignore_index=True)
df

# METHOD 3: LIST COMPREHENSION ----
# - Benefit: Similar to Method 2, but maybe slightly more concise

li_3 = [pd.read_csv(filename, index_col=None, header=0) for filename in all_files]

df = pd.concat(li_3, axis=0, ignore_index=True)
df



# LEARNING MORE:
# Python for Data Science Automation Course: 
# https://university.business-science.io/p/python-for-data-science-automation-ds4b-101p
