import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):


def setUp(self):
    self.myCalc = Calculator(8,2)

    def test_sum(self):

        self.assertEqual(self.myCalc.get_sum(), 10, "Wrong sum")


    def test_quotient(self):

        self.assertEqual(self.myCalc.get_quotient(), 4, "Wrong quotient")

    def test_diff(self):
  
        self.assertEqual(self.myCalc.get_difference(), 6, "Wrong difference")

    def test_product(self):
        
        self.assertEqual(self.myCalc.get_product(), 16, "Wrong product")




    if __name__ == "__main__":

        unittest.main()
