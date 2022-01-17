#!/usr/bin/python

print('prices_process - initiating.')

import os
import pandas as pd

pd.options.mode.chained_assignment = None

# set directories and files
cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
other_folder = "other"

from pathlib import Path
paths = Path(os.path.join(cwd,input_folder,temp_folder,other_folder)).glob('**/*.csv')

prices_table = []
for path in paths:
    path_in_str = str(path)
    try:
        tickers_parse = pd.read_csv(path,low_memory=False)
        prices_table.append(tickers_parse)
        print(path_in_str)
    except:
        pass

# export everything
prices_table = pd.concat(prices_table)
prices_table.drop_duplicates()
prices_table.to_csv(os.path.join(cwd,input_folder,"2_other_updated.csv"), index=False)
prices_table.to_excel(os.path.join(cwd,input_folder,"2_other_updated.xlsx"))

# export columns
df_columns=pd.DataFrame(prices_table.columns.T)
df_columns.to_excel(os.path.join(cwd,input_folder,'2_tickers_narrowed_columns.xlsx'))

print('prices_process - done')