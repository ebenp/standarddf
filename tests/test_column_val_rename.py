# test for column renaming
# 2021-12-01. Written by Eben Pendleton.

import sys
sys.path.append('../..')
from standarddf import standarddf
import pandas as pd

# test for standarddf
if __name__ == "__main__":
    file1 = 'test_df.xlsx'
    file2 = 'test_column_val_rename.xlsx'

    df = standarddf(file1, file2)
    print(df)

    file1 = 'test_df.xls'
    file2 = 'test_column_val_rename.xlsx'

    df = standarddf(file1, file2)
    print(df)

    file1 = 'test_df.csv'
    file2 = 'test_column_val_rename.xlsx'

    df = standarddf(file1, file2)
    print(df)

    file1 = 'test_df.csv'
    file2 = 'test_column_val_rename.xlsx'
    output_file = 'out_test.csv'

    standarddf(file1, file2, output_file)

    file1 = 'test_df.xlsx'
    file2 = 'test_column_val_rename.xlsx'
    output_file = 'out_test.xlsx'

    standarddf(file1, file2, output_file)