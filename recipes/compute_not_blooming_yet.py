# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
days_till_bloom = dataiku.Dataset("days_till_bloom")
days_till_bloom_df = days_till_bloom.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

not_blooming_yet_df = days_till_bloom_df # For this sample code, simply copy input to output


# Write recipe outputs
not_blooming_yet = dataiku.Dataset("not_blooming_yet")
not_blooming_yet.write_with_schema(not_blooming_yet_df)
