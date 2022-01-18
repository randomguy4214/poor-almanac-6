#!/usr/bin/python
print('prices_update - initiating.')

import os
import pandas as pd
from datetime import date
import yahooquery as yq

cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
financials_temp = "financials_quarterly"

#check year
todays_date = date.today()
curr_year = todays_date.year

# prepare tickers, find last batch
df_tickers = pd.read_csv(os.path.join(cwd,"0_symbols.csv"))
prices_last_ticker = pd.read_csv(os.path.join(cwd,input_folder,temp_folder,"prices_last_ticker.csv"),index_col=0)
last_ticker = prices_last_ticker.values[0]
last_ticker_n = last_ticker[0]
print("last batch in prices was", last_ticker_n)

# start importing the prices
index_max = pd.to_numeric(df_tickers.index.values.max())
chunk_size = 100
for t in tickers.split(' '):
    try:
        n = pd.to_numeric(tickers_narrowed["symbol"][tickers_narrowed["symbol"] == t].index).values
        if n > last_ticker_n:

            # download quarterly data
            df_quarter = yq.Ticker(tickers, asynchronous=True).all_financial_data(frequency="q")
            output_quarter = 'df_quarter.xlsx'
            df_quarter.to_excel(os.path.join(cwd, output_quarter))

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
