"""
Graphical User Interface for Roman numeral converter
"""
import tkinter as tk
from tkinter import messagebox
from roman_converter import roman_to_int, int_to_roman

class RomanConverterApp:
    """
    GUI application for Roman numeral conversion
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Roman to Integer Converter")
        self.root.geometry("400x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input field for Roman numeral
        self.label = tk.Label(self.root, text="Enter Roman Numeral:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        
        # Convert button
        self.convert_btn = tk.Button(self.root, text="Convert to Integer", command=self.convert)
        self.convert_btn.pack(pady=10)
        
        # Result display
        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack(pady=10)
        
        # Separator
        separator = tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=10)
        
        # Reverse conversion section
        self.reverse_label = tk.Label(self.root, text="Or enter Integer to convert to Roman:")
        self.reverse_label.pack(pady=5)
        
        self.int_entry = tk.Entry(self.root, width=30)
        self.int_entry.pack(pady=5)
        
        self.reverse_btn = tk.Button(self.root, text="Convert to Roman", command=self.reverse_convert)
        self.reverse_btn.pack(pady=10)
        
        self.roman_result_label = tk.Label(self.root, text="Roman Result: ")
        self.roman_result_label.pack(pady=10)
        
        # Clear button
        self.clear_btn = tk.Button(self.root, text="Clear All", command=self.clear)
        self.clear_btn.pack(pady=10)
    
    def convert(self):
        # Convert Roman to integer
        roman = self.entry.get().strip().upper()
        if not roman:
            messagebox.showerror("Error", "Please enter a Roman numeral")
            return
        
        try:
            result = roman_to_int(roman)
            self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def reverse_convert(self):
        # Convert integer to Roman
        num_str = self.int_entry.get().strip()
        if not num_str:
            messagebox.showerror("Error", "Please enter an integer")
            return
        
        try:
            num = int(num_str)
            result = int_to_roman(num)
            self.roman_result_label.config(text=f"Roman Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def clear(self):
        # Clear all fields
        self.entry.delete(0, tk.END)
        self.int_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")
        self.roman_result_label.config(text="Roman Result: ")

def main():
    """Launch the GUI application"""
    root = tk.Tk()
    app = RomanConverterApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()