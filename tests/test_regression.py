"""
Test for regression.py
"""
import unittest
import pandas as pd
from scripts.regression import perform_regression


class TestRegression(unittest.TestCase):
    def setUp(self):
        """
        Create a sample DataFrame for testing
        """
        data = {
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [10, 20, 30, 40, 50],
            "stress_level": [2, 4, 3, 5, 6],
        }
        self.df = pd.DataFrame(data)

    def test_perform_regression(self):
        """
        Perform test regression but make it save under a different name that the original plot
        """
        perform_regression(
            self.df, output_filename="test_regression_DO_NOT_CONSIDER.png"
        )


if __name__ == "__main__":
    unittest.main()
