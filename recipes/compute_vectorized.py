# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
cherry_blossom_prepared = dataiku.Dataset("cherry_blossom_prepared")
df_data = cherry_blossom_prepared.get_dataframe().sort_values("date", ascending=False)
df_data.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
steps = []
x = []
y = []

## Set the number of historical data points to use to predict future records
window_size = 100

## Create windows of input values
for i in range(len(df_data) - window_size - 1):
    subdf = df_data.iloc[i:i + window_size + 1]
    values = subdf['temperature'].values.tolist()[::-1]
    step = subdf['date'].values.tolist()[0]
    status = subdf['flower_status'].values.tolist()[0]

    x.append(str(values[:-1])) # append the past temperatures except for the one of the current day
    steps.append(step)
    y.append(status)

df_win = pd.DataFrame.from_dict({'date': steps, 'past_temp': x, 'flower_status': y})

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
series_window = dataiku.Dataset("vecrotized")
series_window.write_with_schema(df_win)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

vectorized_df = cherry_blossom_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
vectorized = dataiku.Dataset("vectorized")
vectorized.write_with_schema(vectorized_df)