import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(2,2)
        self.assertEqual(calculation.get_sum(), 4, "The answer is not 4!!")

    if __name__ == "__main__":

        unittest.main()

    def test_quotient(self):
        calculation = Calculator(6,2)
        self.assertEqual(calculation.get_quotient(), 3, "The answer is not 3!!")

    if __name__ == "__main__":

        unittest.main()
