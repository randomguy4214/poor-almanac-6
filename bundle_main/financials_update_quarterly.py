#!/usr/bin/python

print('financials_update_quarterly - initiating. Printing Stock and % Progress.')

import os
import pandas as pd
from datetime import date
import FundamentalAnalysis as fa

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:20,.2f}'.format
pd.options.mode.use_inf_as_na = True

cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
financials_temp = "financials_quarterly"

# CMPcloud API key
API_key_file = pd.read_csv(os.path.join(cwd,"API_key.csv"))
api_key = API_key_file.iloc[0,0]

#check year
todays_date = date.today()
curr_year = todays_date.year

# prepare tickers list
tickers_narrowed = pd.read_csv(os.path.join(cwd,"0_symbols.csv"))
ticker_narrowed = tickers_narrowed.head(4)
ticker_narrowed = tickers_narrowed.values.tolist()
tickers = ' '.join(tickers_narrowed["symbol"].astype(str)).strip()

# find last updated ticker (this is necessary if you lose internet connection, etc)
financials_quarterly_last_ticker = pd.read_csv(os.path.join(cwd,input_folder,temp_folder,"financials_quarterly_last_ticker.csv"),index_col=0)
last_ticker_n = financials_quarterly_last_ticker.values[0]
print("last ticker in financials_quarterly was number ", last_ticker_n)

# start importing
index_max = pd.to_numeric(tickers_narrowed.index.values.max())
financials_table = []
company_info = []

for t in tickers.split(' '):
    try:
        n = pd.to_numeric(tickers_narrowed["symbol"][tickers_narrowed["symbol"] == t].index).values
        if n > last_ticker_n:
            income_statement_quarter_T = income_statement_quarter.T #.head(4)
            income_statement_quarter_T["symbol"] = t
            # print & export last_n
            print(t, n/index_max*100, "% /", n, "from", index_max, " /financials quarterly")
            financials_quarterly_last_ticker = pd.DataFrame({'number':n})
            financials_quarterly_last_ticker.to_csv(os.path.join(cwd, input_folder, temp_folder, "financials_quarterly_last_ticker.csv"))
            # export files
            name = t + ".csv"
            df_merged.to_csv(os.path.join(cwd, input_folder, temp_folder, financials_temp, name), index=False)
    except:
        pass

financials_quarterly_last_ticker = pd.DataFrame({'number': [0]})
financials_quarterly_last_ticker.to_csv(
    os.path.join(cwd, input_folder, temp_folder, "financials_quarterly_last_ticker.csv"))

print('financials_update_quarterly - done')
