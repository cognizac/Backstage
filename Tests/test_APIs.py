import unittest

from database.postgres import getQuery
from publicAPIs import getWeather, getLatLon

class TestAPIs(unittest.TestCase):

    def test_correct_arguments_getWeather(self):
        self.assertRaises(ValueError, getWeather, 'test', 'badinputs')
    def test_correct_arguments_getLatLon(self):
        self.assertRaises(ValueError, getLatLon, 123)
    def test_if_API_call_errors_handled:
        #todo
        pass

if __name__ == '__main__':
    unittest.main()