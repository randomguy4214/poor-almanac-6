#!/usr/bin/python
print('update_prices - initiating.')

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

#check year
todays_date = date.today()
curr_year = todays_date.year

# prepare tickers, find last batch
df_tickers = pd.read_csv(os.path.join(cwd,"0_symbols.csv"))
prices_last_ticker = pd.read_csv(os.path.join(cwd,input_folder,temp_folder,"prices_last_ticker.csv"),index_col=0)
last_ticker = prices_last_ticker.values[0]
last_ticker_n = last_ticker[0]
print("last batch in prices was", last_ticker_n)

# start importing
index_max = pd.to_numeric(df_tickers.index.values.max())
chunk_size = 100
for i in range(last_ticker_n, len(df_tickers), chunk_size):
    try:
        df_chunk = df_tickers[i:i+9]
        index_last = pd.to_numeric(df_chunk.index.values.max())
        tickers_narrowed = df_chunk.values.tolist()
        tickers = ' '.join(df_chunk["symbol"].astype(str)).strip()
        # download
        dict_quotes = yq.Ticker(tickers, asynchronous=True).quotes
        df = pd.DataFrame.from_dict(dict_quotes).T
        print(df)
        df.reset_index(inplace=True, drop=False)
        df.rename(columns={"index": "symbol"}, inplace=True)
        output_string = 'df_quotes_' + str(index_last) + '.csv'
        df.to_csv(os.path.join(cwd,input_folder,temp_folder,prices_temp,output_string))
        # print & export last_n
        nnn = int(index_last/index_max*100)
        print("prices:", index_last, "from", index_max, "/", nnn, "%")
        last_ticker = pd.DataFrame([{'number':index_last}])
        last_ticker.to_csv(os.path.join(cwd, input_folder, temp_folder, "prices_last_ticker.csv"))
    except:
        pass

last_ticker = pd.DataFrame({'number':[0]})
last_ticker.to_csv(os.path.join(cwd,input_folder,temp_folder,"prices_last_ticker.csv"))
print('update_prices - done')
