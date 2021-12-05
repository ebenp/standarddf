
import pandas as pd
import argparse

# Python Function to standardize two dataframes based on multi tabbed Excel file
# 2021-12-01. Written by Eben Pendleton.

def standarddf(file1, file2, output_file = None, sheet_name = 'Sheet1'):
    """
    :param file: file to standardize, If excel sheet_name is used
    :param file: Excel file containing standards
    :param output: (optional): Set output file path. If none, dataframe is returned. csv and xlsx are supported.
    :param sheet_name (optional): Optional sheet_name
    :return:
    """

    # handle column renames
    df_rename = pd.read_excel(file2, sheet_name = "column_rename")
    if '.xls' in file1:
        df = pd.read_excel(file1, sheet_name = sheet_name)
    if '.csv' in file1:
        df = pd.read_csv(file1)
    df.rename(columns = dict(zip(df_rename['old_name'], df_rename['new_name'])), inplace = True)

    # loop through the sheet names and handle any replacement
    dfs = pd.ExcelFile(file2)
    for sn in dfs.sheet_names:
        if sn in df.columns:
            tmp_df = dfs.parse(sn)
            df[sn].replace(to_replace = tmp_df['old_value'].values, value=tmp_df['new_value'].values, inplace = True)

    if output_file is None:
        return df

    if '.csv' in output_file:
        return df.to_csv(output_file, index = False)
    if '.xlsx' in output_file:
        return df.to_excel(output_file, index = False)

# commandline usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Rename columns and replace values in a data table')
    parser.add_argument('f1', metavar='file1', type=str, nargs=1,
                        help='File path of data to standardize')
    parser.add_argument('ef', metavar='file2', type=str, nargs=1,
                        help='Excel file path of data renames')
    parser.add_argument('of', metavar='output_file', type=str, nargs=1,
                        help='Excel file path of data renames')
    parser.add_argument('sn', metavar='sheet_name', type=str, nargs='?',
                        help='Optional sheet name', default=None)
    args = parser.parse_args()
    sheet_name = 'Sheet1'
    if args.sn is not None:
        sheet_name = args.sn

    standarddf(args.f1[0], args.ef[0], output_file=args.of[0], sheet_name = sheet_name)