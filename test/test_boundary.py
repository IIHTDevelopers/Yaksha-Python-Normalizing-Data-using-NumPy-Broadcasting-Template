import unittest
import numpy as np
from mainclass import DataNormalizer
from test.TestUtils import TestUtils
import pandas as pd

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.single_value_scores = [85]  # Single value in the array
        self.normalizer_single_value = DataNormalizer(self.single_value_scores)

    def test_single_value_data(self):
        """Test handling of single value data."""
        test_obj = TestUtils()
        try:
            normalized_scores = self.normalizer_single_value.normalize_data()
            expected_output = np.array([85], dtype=np.float32)  # No change for single value
            if np.array_equal(normalized_scores, expected_output):
                test_obj.yakshaAssert("TestSingleValueData", True, "boundary")
                print("TestSingleValueData = Passed")
            else:
                test_obj.yakshaAssert("TestSingleValueData", False, "boundary")
                print("TestSingleValueData = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestSingleValueData", False, "boundary")
            print(f"TestSingleValueData = Failed: {str(e)}")