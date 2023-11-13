import unittest
from city_functions import city_countrys

class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        name = city_countrys('santiago', 'chile')
        self.assertEqual(name, 'Santiago, Chile')

    def test_city_country_population(self):
        name = city_countrys('santiago', 'chile', '5000000')
        self.assertEqual(name, 'Santiago, Chile - Population 5000000')

unittest.main()