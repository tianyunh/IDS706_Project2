"""Create python library for csv linter helper functions"""
import pandas as pd

# check columns which have no items
def zero_count_columns(df):
    bad_columns = []
    for key in df.keys():
        if df[key].count() == 0:
            bad_columns.append(key)
    return bad_columns


# check if there are any unnamed columns
def unnamed_columns(df):
    bad_columns = []
    for key in df.keys():
        if "Unnamed" in key:
            bad_columns.append(key)
    return len(bad_columns)
    
# check if there are any columns containing NAN
def na_columns(df):
    na_columns = []
    for key in df.keys():
        if df[key].isnull().values.any():
            na_columns.append(key)
    return na_columns


    
