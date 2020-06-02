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