#!/usr/bin/python
print('update_financials_quarterly - initiating.')
import sys, os
import pandas as pd
import yahooquery as yq
import time
cwd = os.getcwd()
input_folder = "0_input"
prices_folder = "data"
output_folder = "0_output"
temp_folder = "temp"
prices_temp = "prices"
financials_temp = "financials_quarterly"
df_tickers = pd.read_csv(os.path.join(cwd, "0_symbols.csv"))
prices_last_ticker = pd.read_csv(os.path.join(cwd, input_folder, temp_folder, "financials_quarterly_last_ticker.csv"), index_col=0)
last_ticker = prices_last_ticker.values[0]
last_ticker_n = last_ticker[0]
print("last batch in quarterly was", last_ticker_n)
print("if no update on screen - change your proxy in settings and/or reduce chunk_size")
print("yahoo allows only 2000 connections per hour from one IP")
print("-//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//-")
index_max = pd.to_numeric(df_tickers.index.values.max())
chunk_size = 100
for i in range(last_ticker_n, len(df_tickers), chunk_size):
    try:
        df_chunk = df_tickers[i:i+chunk_size]
        index_last = pd.to_numeric(df_chunk.index.values.max())
        tickers_narrowed = df_chunk.values.tolist()
        tickers = ' '.join(df_chunk["symbol"].astype(str)).strip()
        # download
        df = yq.Ticker(tickers, asynchronous=True).all_financial_data(frequency="q")
        output_string = 'df_quarter_' + str(index_last) + '.csv'
        df.to_csv(os.path.join(cwd,input_folder,temp_folder,financials_temp,output_string))
        # print & export last_n
        nnn = int(index_last/index_max*100)
        print("quarter:", index_last, "from", index_max, "/", nnn, "%")
        last_ticker = pd.DataFrame([{'number':index_last}])
        last_ticker.to_csv(os.path.join(cwd, input_folder, temp_folder, "financials_quarterly_last_ticker.csv"))
    except:
        print('!!! ERROR !!! change your proxy and/or reduce the chunk_size')
        sys.exit()
        #pass

last_ticker = pd.DataFrame({'number': [0]})
last_ticker.to_csv(
    os.path.join(cwd, input_folder, temp_folder, "financials_quarterly_last_ticker.csv"))
print('update_financials_quarterly - done')
