# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
days_till_bloom = dataiku.Dataset("days_till_bloom")
df = days_till_bloom.get_dataframe().sort_values('date', ascending=False).reset_index(drop=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
length = 100

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['past_temperature'] = np.nan
long_vec = df['temperature'].values.tolist()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for i in range(0, df.shape[0]):
    small_vec = str(long_vec[i+1:i+length][::-1])
    df.loc[i, "past_temperature"]=small_vec

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
not_blooming_yet = dataiku.Dataset("past_temp")
not_blooming_yet.write_with_schema(df)