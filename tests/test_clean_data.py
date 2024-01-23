"""
Test for clean_data.py
"""
import unittest
import pandas as pd
from scripts.clean_data import handle_null_values


class TestHandleNullValues(unittest.TestCase):
    def setUp(self):
        """
        Create a sample DataFrame with null values for testing
        """
        data = {"column1": [1, 2, None, 4, 5], "column2": [10, 20, 30, None, 50]}
        self.df_with_nulls = pd.DataFrame(data)

    def test_handle_null_values(self):
        df_cleaned = handle_null_values(self.df_with_nulls)
        self.assertTrue(df_cleaned.isnull().sum().all() == 0)


if __name__ == "__main__":
    unittest.main()
