#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import numpy as np
import scipy as sp
import scipy as sp
from scipy import stats
from scipy.stats import ttest_ind
import os


plt.figure(figsize=(20,20))
sns.lmplot(x='year', y='per_all_poverty', data=stats_df, fit_reg=False)
plt.xlim(2009,2018)
plt.ylim(0,30)
sns.lmplot(x='year', y='per_all_200k', data=stats_df, fit_reg=False)
plt.xlim(2009,2018)
plt.ylim(0,30)
plt.show()

