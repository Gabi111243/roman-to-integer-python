"""
Validation functions for Roman numerals
"""

def is_valid_roman(s):
    """
    Validate if input is a proper Roman numeral
    """
    if not s or not isinstance(s, str):
        return False
    
    # Check for valid characters only
    valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    if not all(char in valid_chars for char in s.upper()):
        return False
    
    # Check for invalid patterns (basic validation)
    s_upper = s.upper()
    invalid_patterns = [
        "IIII", "XXXX", "CCCC", "MMMM",  # More than 3 repeats
        "VV", "LL", "DD",  # Cannot repeat V, L, or D
        "IL", "IC", "ID", "IM",  # Invalid subtractive combinations
        "VX", "VL", "VC", "VD", "VM",
        "XD", "XM",
        "LC", "LD", "LM"
    ]
    
    for pattern in invalid_patterns:
        if pattern in s_upper:
            return False
    
    return True