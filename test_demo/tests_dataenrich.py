import unittest
from dataenrich import clean_date_column

class TestDataTypes(unittest.TestCase):

    def test_date_column_dtype(self):
        columndatatype = books_df_v01["Book checkout"].dtype
        self.assertIs(columndatatype, 'datetime')

if __name__ == "__main__":
    unittest.main()
        