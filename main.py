"""
Main entry point for Roman numeral converter
"""
import sys
from roman_converter import roman_to_int, int_to_roman
from gui import main as gui_main

def print_usage():
    """Print usage instructions"""
    print("Roman Numeral Converter")
    print("Usage:")
    print("  python main.py <roman_numeral>  # Convert Roman to integer")
    print("  python main.py <integer> --reverse  # Convert integer to Roman")
    print("  python main.py --gui  # Launch graphical interface")
    print("\nExamples:")
    print("  python main.py XIV")
    print("  python main.py 14 --reverse")
    print("  python main.py --gui")

def main():
    """Main function with simple command-line interface"""
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print_usage()
        return
    
    if '--gui' in sys.argv:
        gui_main()
        return
    
    reverse = '--reverse' in sys.argv or '-r' in sys.argv
    
    # Extract the input value (first non-flag argument)
    input_val = None
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            input_val = arg
            break
    
    if not input_val:
        print("Error: No input value provided")
        print_usage()
        return
    
    try:
        if reverse:
            num = int(input_val)
            result = int_to_roman(num)
            print(f"{num} = {result}")
        else:
            result = roman_to_int(input_val.upper())
            print(f"{input_val} = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()