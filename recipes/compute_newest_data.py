# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

newest_data_df = ... # Compute a Pandas dataframe to write into newest_data


# Write recipe outputs
newest_data = dataiku.Dataset("newest_data")
newest_data.write_with_schema(newest_data_df)
