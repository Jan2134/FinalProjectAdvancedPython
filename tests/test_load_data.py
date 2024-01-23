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
        self.path = "datasets/BooksDatasetClean.cs"

    def test_extansion_fail(self):
        """
        Test for extansion of the dataset
        """
        with self.assertRaises(TypeError):
            load_dataset(self.path)


if __name__ == "__main__":
    unittest()
