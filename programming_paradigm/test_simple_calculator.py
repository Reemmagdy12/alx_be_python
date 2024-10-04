import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,2),3)
        self.assertEqual(self.calc.subtract(4,-2),6)
        self.assertEqual(self.calc.subtract(-2,-2),0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,2),10)
        self.assertEqual(self.calc.multiply(-2,2),-4)
        self.assertEqual(self.calc.multiply(-3,-2),6)

    def test_devision(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(-10,2),-5)
        self.assertEqual(self.calc.divide(-10,-2),5)
        self.assertEqual(self.calc.divide(-10,0), None)

if __name__ == "__main__":
   unittest. main()
        
        
    


   