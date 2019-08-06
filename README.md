# steammarket

Python module to quickly get item prices from Steam Marketplace.
# Installation
`pip install steammarket`

OR

```bash
git clone https://github.com/MatyiFKBT/pysteammarket
cd pysteammarket
python setup.py install
```

# Usage

## Example
```python
import steammarket as sm

item = sm.get_tf2_item('Strange Professional Killstreak Scattergun')
for listing in item.listings:
    print(listing.price)
```

## get_item

```python
get_item(appid, name, currency='EUR')
```

Gets item listings from the `Steam Marketplace`.

@appid ID of game item belongs to.

@name: Name of item to lookup.

@currency: Abbreviation of currency to return listing prices in.
Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`

Defaults to `EUR`.
Please lookup the proper abbreviation for your currency of choice.

Returns a json object
Example:

```json
{
    "success": true,
    "lowest_price": "0,92Ç",
    "volume": "15",
    "median_price": "0,80Ç"
}
```

## get_multiple

```python
get_multiple(items, appid=440, currency='EUR')
```

Fetch multiple items using get_item().

## get_tf2_item

```python
get_tf2_item(item, currency='EUR')
```

Fetches an item from TF2. (Defaults the `appid` to 440)

## get_csgo_item

```python
get_csgo_item(item, currency='EUR')
```

Fetches an item from CSGO. (Defaults the `appid` to 730)