import unittest
from segmentation_utils import segment_me

class TestSegmentation(unittest.TestCase):
    def test_segment_me_gold(self):
        df = {'RFM_Score': 12}
        self.assertEqual(segment_me(df), '1.Gold')
        df = {'RFM_Score': 9}
        self.assertEqual(segment_me(df), '1.Gold')

    def test_segment_me_silver(self):
        df = {'RFM_Score': 8.9}
        self.assertEqual(segment_me(df), '2.Silver')
        df = {'RFM_Score': 5}
        self.assertEqual(segment_me(df), '2.Silver')

    def test_segment_me_bronze(self):
        df = {'RFM_Score': 4.9}
        self.assertEqual(segment_me(df), '3.Bronze')
        df = {'RFM_Score': 0}
        self.assertEqual(segment_me(df), '3.Bronze')
        df = {'RFM_Score': -1}
        self.assertEqual(segment_me(df), '3.Bronze')

    def test_segment_me_invalid_types_handled(self):
        # Now handled by returning '3.Bronze'
        self.assertEqual(segment_me({'RFM_Score': None}), '3.Bronze')
        self.assertEqual(segment_me({}), '3.Bronze')
        self.assertEqual(segment_me({'RFM_Score': 'invalid'}), '3.Bronze')

if __name__ == '__main__':
    unittest.main()
