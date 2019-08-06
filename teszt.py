import steammarket as market
import time
import steam_market as _m
items = ['Killstreak Tide Turner','Killstreak Tide Turner Kit']

start = time.time()
res = market.get_multiple(items)
print(time.time()-start,res)