"""
Core conversion functions for Roman numerals
"""

def roman_to_int(s):
    """
    Convert Roman numeral to integer
    """
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    from .validator import is_valid_roman
    if not is_valid_roman(s):
        raise ValueError("Invalid Roman numeral")
    
    total = 0
    prev_value = 0
    
    # Process each character from right to left
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def int_to_roman(num):
    """
    Convert integer to Roman numeral
    """
    if not isinstance(num, int) or num <= 0 or num > 3999:
        raise ValueError("Input must be an integer between 1 and 3999")
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ''
    i = 0
    while num > 0:
        # Add the largest possible symbol
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num