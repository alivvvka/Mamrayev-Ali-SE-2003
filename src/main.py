from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

list = cg.get_coins_markets("usd")[:10]

def myFunc(e):
    return e['market_cap_rank']

list.sort(key=myFunc)

for cur in list:
    print(cur['name'], " | Market rank - ", cur['market_cap_rank'], "Current price - ", cur['current_price'])