import unittest

from database.postgres import getQuery
from publicAPIs import getWeather, getLatLon

class TestAPIs(unittest.TestCase):

    def test_correct_arguments_getWeather(self):
        self.assertRaises(ValueError, getWeather, 'test', 'badinputs')
    def test_correct_arguments_getLatLon(self):
        self.assertRaises(ValueError, getLatLon, 123)

if __name__ == '__main__':
    unittest.main()