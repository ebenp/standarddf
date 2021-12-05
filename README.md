# standarddf
Standardize dataframes using Excel multi sheet input

See an example Excel file under [tests/test_column_val_rename.xlsx](tests/test_column_val_rename.xlsx)

There must be a sheet entitled column_rename that has two columns: new_name and old_name.
Additional sheets with names of new_name and having columns new_value_old_value is an example of value 
replacement

This can be imported as a function

```
from standarddf import standarddf

# returning a dataframe. file1 and file 2 are file paths
df = standarddf(file1, file2)

# with output file path
standarddf(file1, file2, output_file)
```

Commandline usage is also allowed

```
python standarddf.py 'tests/test_df.xlsx' 'tests/test_column_val_rename.xlsx' 'out_test.xlsx'

```