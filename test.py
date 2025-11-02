import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_add(self):
        # Test addition functionality
        result = self.calc.add(3, 7)
        self.assertEqual(result, 10)
        
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)