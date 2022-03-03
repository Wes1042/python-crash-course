
import unittest
from webbrowser import get

from city_functions import get_formatted_cities

class CityTestCase(unittest.TestCase):
    def test_city_countries(self):
        """Does Chile Santiage work?"""
        formatted_city = get_formatted_cities('santiago', 'chile')
        self.assertEqual(formatted_city,'Santiago, Chile')

    def test_city_country_population(self):
        """Can I include a population?"""
        formatted_city = get_formatted_cities('santiago', 'chile' , population=5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')
unittest.main()