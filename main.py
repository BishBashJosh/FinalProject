import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import unittest 
import function
"""
class TestFunction(unittest.TestCase):
    #Running code
    def test_multiply(self):
        result = function.multiply_numbers(20, 9)
        self.assertEqual(result, 180)

    def test_divide(self):
        result = function.divide_numbers(25, 5)
        self.assertEqual(result, 5)
    
    def test_double(self):
        result = function.double_number(25)
        self.assertEqual(result, 50)

    def test_square(self):
        result = function.square_number(9)
        self.assertEqual(result, 81)

if __name__ == '__main__':
    unittest.main()
"""

df_gcse = pd.read_csv('cleansedGcse.csv', encoding = 'UTF-8')
df_income = pd.read_csv('cleansedIncome.csv', encoding = 'UTF-8')

print (df_gcse)
print (df_income)