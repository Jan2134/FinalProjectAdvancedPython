""""
Script for testing stats.py
"""
import unittest
import pandas as pd
from scripts.stats import calculate_correlation_matrix
from unittest.mock import patch


class TestCalculateCorrelationMatrix(unittest.TestCase):
    def setUp(self):
        """
        Create a sample DataFrame for testing
        """
        data = {
            "column1": [1, 2, 3, 4, 5],
            "column2": [10, 20, 30, 40, 50],
            "column3": [5, 4, 3, 2, 1],
        }
        self.df = pd.DataFrame(data)

    @patch(
        "scripts.stats.plt.savefig"
    )  # Mock plt.savefig to avoid saving actual plot files
    def test_calculate_correlation_matrix(self, mock_savefig):
        correlation_matrix, top_correlations_info = calculate_correlation_matrix(
            self.df
        )
        self.assertIsInstance(correlation_matrix, pd.DataFrame)
        self.assertIsInstance(top_correlations_info, dict)


if __name__ == "__main__":
    unittest.main()
