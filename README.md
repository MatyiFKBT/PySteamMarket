# steammarket

Python module to quickly get item prices from Steam Marketplace.

## Installation

`pip install steammarket`

OR

```bash
git clone https://github.com/MatyiFKBT/pysteammarket
cd pysteammarket
python setup.py install
```

## Usage

### Example in TF2

```python
import steammarket as sm

item = sm.get_tf2_item('Strange Professional Killstreak Scattergun')
for listing in item.listings:
    print(listing.price)
```

### set_steamLoginSecure

```python
set_steamLoginSecure(steamLoginSecure)
```

Cookie parameter required for `get_pricehistory()` function
Login to steam on your browser and get your steam login cookie

For Chrome, settings > advanced > content settings > cookies > see all cookies and site data > find steamcommunity.com > find `steamLoginSecure` > copy the `Content` string
For Firefox, Developer Tools > Storage tab > select steamcommunity.com under `Cookies` > find `steamLoginSecure` > copy the `Content` string
Founded string is the @steamLoginSecure

### set_def_currency(currency)

```python
set_def_currency(currency)
```

Sets default currency for functions

@currency: Name of requested currency
Accepted currencies in `curAbbrev`

Defaults to `EUR`
Please lookup the proper abbreviation for your currency of choice.

### get_total_count

```python
get_total_count(appid)
```

Gets total count of items listed in the market

@appid: ID of game item belongs to.

Returns int, -1 if is not successful

### get_item

```python
get_item(appid, name, currency=defaultCurr)
```

Gets item listings from the `Steam Marketplace`.

@appid: ID of game item belongs to.

@name: Name of item to lookup.

@currency: Abbreviation of currency to return listing prices in.
Defaults to @defaultCurr

Returns a json object
Example:
```json
{
	"success": true,
	"lowest_price": "0,92€",
	"volume": "15",
	"median_price": "0,80€"
}
```

### get_render

```python
get_render(appid, count = 100, start = 0)
```

Gets items list of defined appid, default sorted by popular in steam market.

@appid: ID of game item belongs to.

@count: Count of showed items, max is 100 defined by server.

@start: The item number to start showing from.

Returns a json object
Example:
```json
{
	"success": true,
	"start": 0,
	"pagesize": 1,
	"total_count": 16132,
	"searchdata": { ... },
	"results": [
		{
			"name": "Operation Broken Fang Case",
			"hash_name": "Operation Broken Fang Case",
			"sell_listings": 13423,
			"sell_price": 98,
			"sell_price_text": "$0.98",
			"app_icon": "https:\\/\\/cdn.cloudflare.steamstatic.com\\/steamcommunity\\/public\\/images\\/apps\\/730\\/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
			"app_name": "Counter-Strike: Global Offensive",
			"asset_description": { ... },
			"sale_price_text": "$0.94"
		}
	]
}
```

### get_pricehistory

```python
get_pricehistory(appid, name, currency=defaultCurr)
```

Gets price history for item from the `Steam Marketplace`.

@appid: ID of game item belongs to.

@name: Name of item to lookup.

@currency: Abbreviation of currency to return listing prices in.
Defaults to @defaultCurr

**Important!**
Set @cookie as explained in documentation above, else function will not work

Returns a json object
Example:
```json
{
	"success": true,
	"lowest_price": "0,92€",
	"volume": "15",
	"median_price": "0,80€"
}
```
	
### get_multiple

```python
get_multiple(items, appid=440, currency=defaultCurr)
```

Fetch multiple items using `get_item()`.

### get_tf2_item

```python
get_tf2_item(item, currency=defaultCurr)
```

Fetches an item from TF2. (Defaults the `appid` to 440)

### get_csgo_item

```python
get_csgo_item(item, currency=defaultCurr)
```

Fetches an item from CSGO. (Defaults the `appid` to 730)
