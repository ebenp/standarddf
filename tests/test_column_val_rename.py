# test for column renaming
# 2021-12-01. Written by Eben Pendleton.

import sys
sys.path.append('../..')
from standarddf import standarddf
import pandas as pd

# test for standarddf
if __name__ == "__main__":

    df = pd.DataFrame({'Colors': ['red', 'yellow', 'green'], "Numbers": [1,2,3]})
    print(df)

    file = "test_column_val_rename.xlsx"

    df = standarddf(df, file)
    print(df)
