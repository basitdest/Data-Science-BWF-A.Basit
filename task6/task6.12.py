# task6.12.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
