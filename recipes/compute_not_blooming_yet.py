# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
days_till_bloom = dataiku.Dataset("days_till_bloom")
df = days_till_bloom.get_dataframe().sort_values('date', ascending=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
new_df = pd.DataFrame()
for year in df.year.unique():
    for index, row in df.iterrows():
        if row['flower_status']!='bloom':
            new_df = new_df.append(row, ignore_index=False)
        else:
            break

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
not_blooming_yet = dataiku.Dataset("not_blooming_yet")
not_blooming_yet.write_with_schema(new_df)