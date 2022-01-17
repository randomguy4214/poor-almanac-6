#!/usr/bin/python

print('other_update - initiating.')

import os
import pandas as pd
from datetime import date
import FundamentalAnalysis as fa

# formatting
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:20,.2f}'.format
pd.options.mode.use_inf_as_na = True

cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
financials_temp = "financials"
other_folder = "other"

# CMPcloud API key
API_key_file = pd.read_csv(os.path.join(cwd,"API_key.csv"))
api_key = API_key_file.iloc[0,0]

#check year
todays_date = date.today()
curr_year = todays_date.year

# prepare tickers list
tickers_narrowed = pd.read_csv(os.path.join(cwd,"0_symbols.csv"))
ticker_narrowed = tickers_narrowed.values.tolist()
ticker_narrowed = tickers_narrowed.head(4)
tickers = ' '.join(tickers_narrowed["symbol"].astype(str)).strip()

# find last updated ticker (this is necessary if you lose internet connection, etc)
prices_last_ticker = pd.read_csv(os.path.join(cwd,input_folder,temp_folder,"other_last_ticker.csv"),index_col=0)
last_ticker_n = prices_last_ticker.values[0]
print("last ticker in prices update was number ", last_ticker_n)

# start importing the prices
index_max = pd.to_numeric(tickers_narrowed.index.values.max())
company_info = []

for t in tickers.split(' '):
    try:
        n = pd.to_numeric(tickers_narrowed["symbol"][tickers_narrowed["symbol"] == t].index).values
        if n > last_ticker_n:
            df = fa.key_metrics(t, api_key)
            df_T = df.T
            df_T.reset_index(drop=False,inplace=True)
            df_T["symbol"] = t
            name = t + ".csv"
            df_T.to_csv(os.path.join(cwd, input_folder, temp_folder, other_folder, name), index=True)

            # print & export last_n
            print(t, n/index_max*100, "% /", n, "from", index_max, " /other")
            prices_last_ticker = pd.DataFrame({'number':n})
            prices_last_ticker.to_csv(os.path.join(cwd, input_folder, temp_folder, "other_last_ticker.csv"))
    except:
        pass

prices_last_ticker = pd.DataFrame({'number': [0] })
prices_last_ticker.to_csv(os.path.join(cwd,input_folder,temp_folder,"other_last_ticker.csv"))

print('other_update - done')
