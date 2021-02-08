# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
blooming_days_joined = dataiku.Dataset("blooming_days_joined")
df = blooming_days_joined.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
d = {}
for year in df.year.unique():
    blooming_day = df[df.year==year].blooming_day.unique()[0]
    d[year] = blooming_day

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
d

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_bloom = df[df.flower_status=='bloom']
df_bloom.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_new = pd.DataFrame()
for year in df.year.unique():
    df_sub = df[df.year==year]
    df_sub['blooming_day_shift'] = df_sub["blooming_day"]
    blooming_ind = df_bloom[df_bloom.year==year].index[0]
    if year < 2019:
        df_sub.loc[df_sub.index > blooming_ind, "blooming_day_shift"] = d[year+1]
    else:
        None
    df_new = pd.concat([df_new, df_sub])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
blooming_days_fixed = dataiku.Dataset("blooming_days_shifted")
blooming_days_fixed.write_with_schema(df_new)