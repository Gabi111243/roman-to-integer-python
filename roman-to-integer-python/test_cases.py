import unittest
from roman_converter import Solution

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.converter = Solution()

    def test_cases(self):
        self.assertEqual(self.converter.romanToInt("III"), 3)
        self.assertEqual(self.converter.romanToInt("IX"), 9)
        self.assertEqual(self.converter.romanToInt("LVIII"), 58)
        self.assertEqual(self.converter.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.converter.romanToInt("XI"), 11)
        self.assertEqual(self.converter.romanToInt("CDXLIV"), 444)

if __name__ == '__main__':
    unittest.main()
