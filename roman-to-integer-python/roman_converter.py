class Solution(object):
    def romanToInt(self, s):
        """
        Convert a Roman numeral to an integer.
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        previous_value = 0

        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < previous_value:
                total -= current_value
            else:
                total += current_value
            previous_value = current_value

        return total

# Example usage
if __name__ == "__main__":
    converter = Solution()
    print(converter.romanToInt("XI"))  # Output: 11
