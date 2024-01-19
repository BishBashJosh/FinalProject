import unittest 
import function
class TestFunction(unittest.TestCase):
    #Running code
    def test_multiply(self):
        result = function.multiply_numbers(20, 9)
        self.assertEqual(result, 180)

if __name__ == '__main__':
    unittest.main()