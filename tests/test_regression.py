"""
Test for regression.py
"""
import unittest
import pandas as pd
from scripts.regression import perform_regression


class TestRegression(unittest.TestCase):

    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        "feature3": [5, 4, 3, 2, 1],
        'stress_level': [2, 4, 3, 5, 6]
    }

    df = pd.DataFrame(data)

    def test_perform_regression(self):
        # Perform regression analysis
        perform_regression(self.df, output_filename="test_regression_DO_NOT_CONSIDER.png")

if __name__ == '__main__':
    unittest.main()
