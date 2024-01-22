"""
Test for the filering module
"""

import unittest
import pandas as pd
from scripts.filtering import Filtering

class TestFilteringMethods(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'column1': [1, 2, 3, 4, 5], 'column2': [10, 20, 30, 40, 50]})

    def test_bigger_than(self):
        filtered_df = Filtering.bigger_than(self.df, 'column1', 3)
        expected_result = pd.DataFrame({'column1': [4, 5], 'column2': [40, 50]})
        expected_result.reset_index(drop=True, inplace=True)
        filtered_df.reset_index(drop=True, inplace=True)
        pd.testing.assert_frame_equal(filtered_df, expected_result)

    def test_smaller_than(self):
        filtered_df = Filtering.smaller_than(self.df, 'column2', 30)
        expected_result = pd.DataFrame({'column1': [1, 2, 3], 'column2': [10, 20, 30]})
        expected_result.reset_index(drop=True, inplace=True)
        filtered_df.reset_index(drop=True, inplace=True)
        pd.testing.assert_frame_equal(filtered_df, expected_result)

if __name__ == '__main__':
    unittest.main()
