import unittest
import weather


class FindIndexTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None

    def test_find_index_positive(self):
        input_list = [49, 57, 56, 55, 53]
        value = 57
        expected_result = 1
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_negative(self):
        input_list = [-10, -8, 2, -16, 4]
        value = 4
        expected_result = 4
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_floats(self):
        input_list = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
        value = 14.5
        expected_result = 1
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_strings(self):
        input_list = ["49", "57", "56", "55", "53", "49"]
        value = "57"
        expected_result = 1
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_empty_list(self):
        input_list = []
        value = ""
        expected_result = None
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_repeated_value(self):
        input_list = [49, 57, 56, 55, 57, 53, 49]
        value = 57
        expected_result = 4
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)

    def test_find_index_string_list(self):
        input_list = ["apple", "banana", "apple", "cherry", "apple", "banana"]
        value = "banana"
        expected_result = 5
        result = weather.find_last_value_in_list(input_list,value)
        self.assertEqual(result, expected_result)    
