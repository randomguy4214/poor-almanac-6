# poor-almanac-6

All I want to know is where I'm going to die, so I'll never go there.

So, yahooquery allows to download in bulk* info from Yahoo!Finance website regaring the companies.
The catch is, you are still very limited by number of connections to Yahoo. In particular, its 2000 per hour.

Yahooquery is doing an excellent job if you are within that limit. Literally 5 seconds download for 10000 tickers.
But if you are above the limit, you need to divide the query into chunks, and reconnect every time to new VPN as soon as you hit the limit.
So, having a proxy implementation like in yfinance would be great. But i didnt see it working.
Therefore, you are own your own. Run the codes in order and see for yourself.

Good luck.
