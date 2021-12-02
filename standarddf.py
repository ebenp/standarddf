
import pandas as pd
# Python Function to standardize two dataframes based on multi tabbed Excel file
# 2021-12-01. Written by Eben Pendleton.

def standarddf(df, file):
    """
    :param df: dataframe to standardize
    :param file: Excel file containing standards
    :return:
    """

    # handle column renames
    df_rename = pd.read_excel(file, sheet_name = "column_rename")
    df.rename(columns = dict(zip(df_rename['old_name'], df_rename['new_name'])), inplace = True)

    # loop through the sheet names and handle any replacement
    dfs = pd.ExcelFile(file)
    for sn in dfs.sheet_names:
        if sn in df.columns:
            tmp_df = dfs.parse(sn)
            df[sn].replace(to_replace = tmp_df['old_value'].values, value=tmp_df['new_value'].values, inplace = True)

    return df