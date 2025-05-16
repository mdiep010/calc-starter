import unittest
import sys
from operations import add, sub, mult, div

class TestAdd(unittest.TestCase): 
    def testAdd(self): 
        calculation = add(8,2)
        self.assertEqual(calculation, 10, 'The sum operation is correct.')

class TestAddZero(unittest.TestCase): 
    def testAdd(self): 
        calculation = add(9,0)
        self.assertEqual(calculation, 9, 'The sum operation is correct.')

class TestAddNeg(unittest.TestCase): 
    def testAdd(self): 
        calculation = add(-4,-2)
        self.assertEqual(calculation, -6, 'The sum operation is correct.')
    
class TestMult(unittest.TestCase): 
    def testAdd(self): 
        calculation = mult(2,4)
        self.assertEqual(calculation, 8, 'The mult operation is correct.')
    
class TestMultZero(unittest.TestCase): 
    def testAdd(self): 
        calculation = mult(0,6)
        self.assertEqual(calculation, 0, 'The mult operation is correct.')

class TestMultNeg(unittest.TestCase): 
    def testAdd(self): 
        calculation = mult(2,-6)
        self.assertEqual(calculation, -12, 'The mult operation is correct.')
    
class TestDivEven(unittest.TestCase): 
    def testAdd(self): 
        calculation = div(8,2)
        self.assertEqual(calculation, 4, 'The div operation is correct.')
    
class TestDivOdd(unittest.TestCase): 
    def testAdd(self): 
        calculation = div(5,2)
        self.assertEqual(calculation, 2.5, 'The div operation is correct.')

class TestDivNeg(unittest.TestCase): 
    def testAdd(self): 
        calculation = div(8,-2)
        self.assertEqual(calculation, -4, 'The div operation is correct.')
    
    
class TestDivZero(unittest.TestCase): 
    def testAdd(self): 
        calculation = div(0,8)
        self.assertEqual(calculation, 0, 'The div operation is correct.')

class TestSub(unittest.TestCase): 
    def testAdd(self): 
        calculation = sub(3,8)
        self.assertEqual(calculation, -5, 'The sub operation is correct.')

class TestSubNeg(unittest.TestCase): 
    def testAdd(self): 
        calculation = sub(-3,-8)
        self.assertEqual(calculation, 5, 'The sub operation is correct.')

class TestSubZero(unittest.TestCase): 
    def testAdd(self): 
        calculation = sub(0,4)
        self.assertEqual(calculation, -4, 'The sub operation is correct.')


if __name__ == '__main__':
    unittest.main()