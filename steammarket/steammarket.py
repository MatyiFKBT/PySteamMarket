import requests, urllib

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
    @param name: Name of item to lookup.
    @param currency: Abbreviation of currency to return listing prices in.
    @type currency:
        Accepted currencies:
        - USD
        - GBP
        - EUR
        - CHF
        - RUB
        - KRW
        - CAD
        Defaults to EUR.
        Please lookup the proper abbreviation for your currency of choice.
    @return A json object with the lowest price,volume, and median price of the chosen item.
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
    return get_item('440', item, currency)
def get_csgo_item(item, currency='EUR'):
    return get_item('730', item, currency)