"""
Unit tests for the Roman numeral converter
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from roman_converter import roman_to_int, int_to_roman, is_valid_roman

class TestRomanConverter(unittest.TestCase):
    """
    Unit tests for the conversion functions
    """
    
    def test_roman_to_int_basic(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)
    
    def test_int_to_roman_basic(self):
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(58), 'LVIII')
        self.assertEqual(int_to_roman(1994), 'MCMXCIV')
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            roman_to_int('IIII')  # Invalid Roman
        with self.assertRaises(ValueError):
            roman_to_int('ABC')   # Invalid characters
        with self.assertRaises(ValueError):
            int_to_roman(0)       # Number too small
        with self.assertRaises(ValueError):
            int_to_roman(4000)    # Number too large
    
    def test_validation(self):
        self.assertTrue(is_valid_roman('III'))
        self.assertTrue(is_valid_roman('XIV'))
        self.assertTrue(is_valid_roman('MCMXC'))
        
        self.assertFalse(is_valid_roman('IIII'))  # Too many I's
        self.assertFalse(is_valid_roman('VV'))    # V cannot repeat
        self.assertFalse(is_valid_roman('IC'))    # Invalid subtraction
        self.assertFalse(is_valid_roman('ABC'))   # Invalid characters
    
    def test_conversion_consistency(self):
        # Test that converting both ways gives original value
        for i in range(1, 100):
            roman = int_to_roman(i)
            result = roman_to_int(roman)
            self.assertEqual(i, result)

if __name__ == '__main__':
    unittest.main()