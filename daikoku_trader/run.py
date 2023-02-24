from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
import pandas as pd
import os

SEC_KEY = os.environ.get('AL_SEC')
PUB_KEY = os.environ.get('AL_PUB')
BASE_URL = 'https://paper-api.alpaca.markets'
trading_client = TradingClient(PUB_KEY, SEC_KEY, paper=True)

symb = "SPY" # The stock symbol we want to trade
# SPY is the ticker symbol for the S&P 500 index

# Getting account information and printing it
# account = trading_client.get_account()
# for property_name, value in account:
#   print(f"\"{property_name}\": {value}")
  
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)
# print(assets)

assets_dict = [dict(item) for item in assets]
df = pd.DataFrame.from_records(assets_dict)
print(df.head(10))

# tutorial: https://analyzingalpha.com/alpaca-markets-api-python-tutorial
# Need to read from beginning

# while True:
#     print("")
#     print("Checking Price")
    
#     market_data = api.get_barset(symb, 'minute', limit=5) # Get one bar object for each of the past 5 minutes

#     close_list = [] # This array will store all the closing prices from the last 5 minutes
#     for bar in market_data[symb]:
#         close_list.append(bar.c) # bar.c is the closing price of that bar's time interval

#     close_list = np.array(close_list, dtype=np.float64) # Convert to numpy array
#     ma = np.mean(close_list)
#     last_price = close_list[4] # Most recent closing price

#     print("Moving Average: " + str(ma))
#     print("Last Price: " + str(last_price))

    
#     if ma + 0.1 < last_price and not pos_held: # If MA is more than 10cents under price, and we haven't already bought
#         print("Buy")
#         api.submit_order(
#             symbol=symb,
#             qty=1,
#             side='buy',
#             type='market',
#             time_in_force='gtc'
#         )
#         pos_held = True
#     elif ma - 0.1 > last_price and pos_held: # If MA is more than 10cents above price, and we already bought
#         print("Sell")
#         api.submit_order(
#             symbol=symb,
#             qty=1,
#             side='sell',
#             type='market',
#             time_in_force='gtc'
#         )
#         pos_held = False
     
#     time.sleep(60)