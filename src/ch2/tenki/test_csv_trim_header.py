import unittest
import pandas as pd

class TestCsvTrimHeader(unittest.TestCase):
    
    def test_trim(self):
        import csv_trim_header as cth
        df = pd.read_csv(cth.out_file, encoding="utf-8")
        v = int(df['年'][0:1][0])
        self.assertEqual(v, 2006)

if __name__ == '__main__':
    unittest.main()
