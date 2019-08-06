import requests

'''
TODO:
  * add all currencies supported by the Steam Marketplace to `curAbbrev`
  * create docstrings for all functions
  * listings parser; get total number of listings (`total_count` in JSON)
  * get price overview via http://steamcommunity.com/market/priceoverview/
'''

# Currency abbreviations
curAbbrev = {
    'USD' : 1,
    'GBP' : 2,
    'EUR' : 3,
    'CHF' : 4,
    'RUB' : 5,
    'KRW' : 16,
    'CAD' : 20,
}

def get_item(appid, name, currency='EUR'):
    r"""
    Gets item listings from the `Steam Marketplace`.

    @appid ID of game item belongs to.

    @name: Name of item to lookup.
    
    @currency: Abbreviation of currency to return listing prices in.
    Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`
    
    Defaults to `EUR`.
    Please lookup the proper abbreviation for your currency of choice.
    
    Returns a json object
    Example:
    ```
    {
        "success": true,
        "lowest_price": "0,92€",
        "volume": "15",
        "median_price": "0,80€"
    }
    ```
    """
    url = 'http://steamcommunity.com//market/priceoverview'
    market_item = requests.get(url,params={
        'appid': appid,
        'market_hash_name': name,
        'currency': curAbbrev[currency]        
    })
    return market_item.json()

def get_multiple(items,appid=440,currency='EUR'):
    """Fetch multiple items using get_item()."""
    result ={}
    for item in items:
        result[item] = get_item(appid,item,currency)
    return result
def get_tf2_item(item, currency='EUR'):
    """Fetches an item from TF2. (Defaults the `appid` to 440)"""
    return get_item('440', item, currency)
def get_csgo_item(item, currency='EUR'):
    """Fetches an item from CSGO. (Defaults the `appid` to 730)"""
    return get_item('730', item, currency)