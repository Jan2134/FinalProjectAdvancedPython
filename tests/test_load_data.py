"""
Run test for the dataset
"""

import unittest
from scripts.main_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    Class to test the dataset inout in different ways
    """

    def setUp(self):
        """
        Path to dataset
        """
        self.path = "dataset/StressLevelDataset.csv"

    def test_extansion_fail(self):
        """
        Test for extension of the dataset
        """
        with self.assertRaises(TypeError) as context:
            load_dataset("dataset/StressLevelDataset.xlsx")

        self.assertIn("Invalid extension", str(context.exception))


if __name__ == "__main__":
    unittest()
