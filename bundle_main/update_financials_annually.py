#!/usr/bin/python

print('financials_update_annually - initiating. Printing Stock and % Progress.')

import os
import pandas as pd
from datetime import date
import yahooquery as yq

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:20,.2f}'.format
pd.options.mode.use_inf_as_na = True

cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
financials_temp = "financials_annually"

#check year
todays_date = date.today()
curr_year = todays_date.year

# prepare tickers list
tickers_narrowed = pd.read_csv(os.path.join(cwd,"0_symbols.csv"))
ticker_narrowed = tickers_narrowed.values.tolist()
tickers = ' '.join(tickers_narrowed["symbol"].astype(str)).strip()

# find last updated ticker (this is necessary if you lose internet connection, etc)
prices_last_ticker = pd.read_csv(os.path.join(cwd,input_folder,temp_folder,"financials_annually_last_ticker.csv"),index_col=0)
last_ticker_n = prices_last_ticker.values[0]
print("last ticker in financials annually was number ", last_ticker_n)

# start importing
index_max = pd.to_numeric(tickers_narrowed.index.values.max())
financials_table = []
company_info = []
for t in tickers.split(' '):
    try:
        n = pd.to_numeric(tickers_narrowed["symbol"][tickers_narrowed["symbol"] == t].index).values
        if n > last_ticker_n:

            # download annual data
            df_annual = yq.Ticker(tickers, asynchronous=True).all_financial_data(frequency="a")
            output_annual = 'df_annual.xlsx'
            df_annual.to_excel(os.path.join(cwd, output_annual))

            # print & export last_n
            print(t, n/index_max*100, "% /", n, "from", index_max, " /financials annually")
            financials_annually_last_ticker = pd.DataFrame({'number': n})
            financials_annually_last_ticker.to_csv(
                os.path.join(cwd, input_folder, temp_folder, "financials_annually_last_ticker.csv"))

    except:
        pass

financials_annually_last_ticker = pd.DataFrame({'number': [0]})
financials_annually_last_ticker.to_csv(
    os.path.join(cwd, input_folder, temp_folder, "financials_annually_last_ticker.csv"))

print('financials_update_annually - done')