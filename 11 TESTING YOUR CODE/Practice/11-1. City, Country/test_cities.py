import unittest
from city_functions import city_countrys

class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        name = city_countrys('santiago', 'chile')
        self.assertEqual(name, 'Santiago, Chile')

unittest.main()