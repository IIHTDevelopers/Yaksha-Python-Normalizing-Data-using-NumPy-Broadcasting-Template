import unittest
import numpy as np
from mainclass import DataNormalizer
from test.TestUtils import TestUtils
import pandas as pd


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.scores = [80, 90, 85, 70, 95]
        self.normalizer = DataNormalizer(self.scores)

    def test_normalize_data(self):
        """Test if the data is normalized correctly."""
        test_obj = TestUtils()
        try:
            normalized_scores = self.normalizer.normalize_data()
            mean = np.mean(normalized_scores)
            std = np.std(normalized_scores)
            
            if np.isclose(mean, 0.0) and np.isclose(std, 1.0):
                test_obj.yakshaAssert("TestNormalizeData", True, "functional")
                print("TestNormalizeData = Passed")
            else:
                test_obj.yakshaAssert("TestNormalizeData", False, "functional")
                print("TestNormalizeData = Failed")
        except:
            test_obj.yakshaAssert("TestNormalizeData", False, "functional")
            print("TestNormalizeData = Failed")