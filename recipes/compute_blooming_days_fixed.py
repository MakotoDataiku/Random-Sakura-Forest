# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
blooming_days_joined = dataiku.Dataset("blooming_days_joined")
blooming_days_joined_df = blooming_days_joined.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

blooming_days_fixed_df = blooming_days_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
blooming_days_fixed = dataiku.Dataset("blooming_days_fixed")
blooming_days_fixed.write_with_schema(blooming_days_fixed_df)
