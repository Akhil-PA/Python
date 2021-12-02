import pandas as pd
from pycoingecko import CoinGeckoAPI
c=CoinGeckoAPI()
bdata=c.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)
prices = pd.DataFrame(bdata['prices'], columns=['TimeStamp', 'Price']).set_index('TimeStamp')
market_caps = pd.DataFrame(bdata['market_caps'], columns=['TimeStamp', 'Market Cap']).set_index('TimeStamp')
total_volumes = pd.DataFrame(bdata['total_volumes'], columns=['TimeStamp', 'Total Volumes']).set_index('TimeStamp')

# combine the separate dataframes
df_market = pd.concat([prices, market_caps, total_volumes], axis=1)

# convert the index to a datetime dtype
df_market.index = pd.to_datetime(df_market.index, unit='ms')
print(df_market)
