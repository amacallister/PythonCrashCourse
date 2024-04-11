import unittest
from city_functions import get_formatted_name

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py"""

    def test_city_country(self):
        """Do names like 'Santiago, Chile' work?"""
        formatted_str = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_str, 'Santiago, Chile')

    def test_city_population(self):
        """Do names like 'City, Country – population xxx' work?"""
        formatted_str = get_formatted_name('santiago', 'chile', 300)
        self.assertEqual(formatted_str, 'Santiago, Chile - Population 300')

if __name__ == '__main__':
    unittest.main()