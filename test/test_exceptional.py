import unittest
from mainclass import DataNormalizer
from test.TestUtils import TestUtils
import numpy as np
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.empty_scores = []
        self.invalid_data = "invalid_data"  # This should raise an error
        self.normalizer_empty = DataNormalizer(self.empty_scores)

    def test_empty_data(self):
        """Test handling of empty data."""
        test_obj = TestUtils()
        try:
            self.normalizer_empty.normalize_data()
            test_obj.yakshaAssert("TestEmptyData", False, "exceptional")
            print("TestEmptyData = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyData", True, "exceptional")
            print("TestEmptyData = Passed")

    def test_invalid_data_type(self):
        """Test handling of invalid data type."""
        test_obj = TestUtils()
        try:
            self.normalizer_invalid = DataNormalizer(self.invalid_data)
            test_obj.yakshaAssert("TestInvalidDataType", False, "exceptional")
            print("TestInvalidDataType = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestInvalidDataType", True, "exceptional")
            print("TestInvalidDataType = Passed")
