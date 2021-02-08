# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
cherry_blossom_prepared = dataiku.Dataset("cherry_blossom_prepared")
cherry_blossom_prepared_df = cherry_blossom_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

vectorized_df = cherry_blossom_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
vectorized = dataiku.Dataset("vectorized")
vectorized.write_with_schema(vectorized_df)
