import requests

defaultCurr = "EUR"

# Login to steam on your browser and get your steam login cookie 
# For Chrome, settings > advanced > content settings > cookies > see all cookies and site data > find steamcommunity.com > find "steamLoginSecure" > copy the "Content" string and paste below
# For Firefox, Developer Tools > Storage tab > select steamcommunity.com under "Cookies." > find "steamLoginSecure" > copy the "Content" string and paste below
cookie = {'steamLoginSecure': 'YOUR_steamLoginSecure'}


# Currency abbreviations
curAbbrev = {
    'USD' : 1,
	'GBP' : 2,
	'EUR' : 3,
	'CHF' : 4,
	'RUB' : 5,
	'PLN' : 6,
	'BRL' : 7,
	'JPY' : 8,
	'NOK' : 9,
	'IDR' : 10,
	'MYR' : 11,
	'PHP' : 12,
	'SGD' : 13,
	'THB' : 14,
	'VND' : 15,
	'KRW' : 16,
	'TRY' : 17,
	'UAH' : 18,
	'MXN' : 19,
	'CAD' : 20,
	'AUD' : 21,
	'NZD' : 22,
	'CNY' : 23,
	'INR' : 24,
	'CLP' : 25,
	'PEN' : 26,
	'COP' : 27,
	'ZAR' : 28,
	'HKD' : 29,
	'TWD' : 30,
	'SAR' : 31,
	'AED' : 32,
	'ARS' : 34,
	'ILS' : 35,
	'BYN' : 36,
	'KZT' : 37,
	'KWD' : 38,
	'QAR' : 39,
	'CRC' : 40,
	'UYU' : 41,
	'RMB' : 9000,
	'NXP' : 9001,
}

    
def set_steamLoginSecure(steamLoginSecure):
    r"""Cookie parameter required for get_pricehistory() function
    Login to steam on your browser and get your steam login cookie
    
    For Chrome, settings > advanced > content settings > cookies > see all cookies and site data > find steamcommunity.com > find "steamLoginSecure" > copy the "Content" string
    For Firefox, Developer Tools > Storage tab > select steamcommunity.com under "Cookies." > find "steamLoginSecure" > copy the "Content" string
    Founded string is the @steamLoginSecure
    """
    cookie["steamLoginSecure"] = steamLoginSecure

def set_def_currency(currency):
    r"""
    Sets default currency for functions

    @currency: Name of requested currency
    Accepted currencies in `curAbbrev`

    Defaults to `EUR`
    Please lookup the proper abbreviation for your currency of choice.
    """
    if currency in curAbbrev.keys():
        defaultCurr = currency
        print("Default currency changed to " + currency)
    else:
        print("Currency is not available")

def get_total_count(appid):
    r"""
    Gets total count of items listed in the market

    @appid: ID of game item belongs to.

    Returns int, -1 if not successful
    """
    f = get_render(appid, count = 0, start = 100000)
    if f and f["success"]:
        return f["total_count"]
    else:
        return -1

def get_item(appid, name, currency = defaultCurr):
    r"""
    Gets item listings from the `Steam Marketplace`.

    @appid: ID of game item belongs to.

    @name: Name of item to lookup.
    
    @currency: Abbreviation of currency to return listing prices in.
    Defaults to @defaultCurr
    
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
    url = 'http://steamcommunity.com/market/priceoverview'
    market_item = requests.get(url,params = {
        'appid': appid,
        'market_hash_name': name,
        'currency': curAbbrev[currency]        
    })
    return market_item.json()

def get_render(appid, count = 100, start = 0):
    r"""
    Gets items list of defined appid, default sorted by popular in steam market.

    @appid: ID of game item belongs to.

    @count: Count of showed items, max is 100 defined by server.

    @start: The item number to start showing from.
    
    Returns a json object
    Example:
    ```
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
    """
    url = 'https://steamcommunity.com/market/search/render'
    render = requests.get(url, params = {
        'appid': appid,
        'norender': 1,
        'count': count,
        'start': start
    })
    return render.json()    

def get_multiple(items, appid, currency = defaultCurr):
    """Fetch multiple items using get_item()."""
    result ={}
    for item in items:
        result[item] = get_item(appid, item, currency)
    return result

def get_pricehistory(appid, name, currency = defaultCurr):
    r"""
    Gets price history for item from the `Steam Marketplace`.

    @appid: ID of game item belongs to.

    @name: Name of item to lookup.

    @currency: Abbreviation of currency to return listing prices in.
    Defaults to @defaultCurr
    
    Important!
    Set @cookie as explained in documentation above, else function will not work
    
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
    if cookie['steamLoginSecure']=='YOUR_COOKIE':
        print("Set steamLoginSecure using set_steamLoginSecure() function as in set_steamLoginSecure.__doc__")
        return []
    else:
        url = 'https://steamcommunity.com/market/pricehistory'
        price_history = requests.get(url, params = {
            'appid': appid,
            'market_hash_name': name,
            'currency': curAbbrev[currency]        
        }, cookies=cookie)
        return price_history.json()

def get_tf2_item(item, currency = defaultCurr):
    """Fetches an item from TF2. (Defaults the `appid` to 440)"""
    return get_item('440', item, currency)

def get_csgo_item(item, currency = defaultCurr):
    """Fetches an item from CSGO. (Defaults the `appid` to 730)"""
    return get_item('730', item, currency)