import steammarket as market
import time
import json
import steam_market as _m
items = ['Killstreak Tide Turner','Killstreak Tide Turner Kit']

# start = time.time()
# res = market.get_multiple(items)
# print(time.time()-start,res)
print(json.dumps(market.get_tf2_item(items[0]),indent=2))