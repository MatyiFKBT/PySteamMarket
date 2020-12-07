import unittest
import steammarket as sm

class TestTF2Items(unittest.TestCase):
    def runTest(self):
        tf2_items = [
            'Strange Professional Killstreak Minigun',
            'Vintage Gunboats',
            'Name Tag',
            'Mann Co. Supply Crate Key'
        ]

        csgo_items = [
            'Gamma Case',
            '\u2605 Karambit | Bright Water (Factory New)',
            'AK-47 | Frontside Misty (Field-Tested)'
        ]

        print('Testing TF2 Items:\n')
        for item in tf2_items:
            print(item)
            market_item = sm.get_tf2_item(item)
            print(market_item["lowest_price"])

        print('\nTesting CS:GO Items:\n')
        for item in csgo_items:
            print(item)
            market_item = sm.get_csgo_item(item)
            print(market_item["lowest_price"])

        print('\nTesting render function for CS:GO Items:\n')
        csgo_render = sm.get_render(730, count=1, start=0)
        print(csgo_render["results"][0]["name"])
        
        print('\nTesting total count of listed items from CS:GO\n')
        print(sm.get_total_count(730))