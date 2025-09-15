# Roman to Integer Converter in Python 🏛️

![GitHub release](https://img.shields.io/github/release/Gabi111243/roman-to-integer-python.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen.svg)

Welcome to the **Roman to Integer Converter** repository! This project provides a comprehensive solution for converting between Roman numerals and integers using Python. Featuring multiple interfaces and validation, this tool is perfect for both educational purposes and practical use.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [Repo Structure](#repo-structure)
- [License](#license)
- [Releases](#releases)

## Introduction

Roman numerals have been used for centuries and are still relevant today. This project aims to bridge the gap between ancient numeral systems and modern programming. By converting between Roman numerals and integers, you can easily perform calculations and data manipulations.

## Installation

To get started with this project, you need to have Python 3.8 or higher installed on your machine. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

Once you have Python installed, you can clone this repository using the following command:

```bash
git clone https://github.com/Gabi111243/roman-to-integer-python.git
```

Navigate to the project directory:

```bash
cd roman-to-integer-python
```

You can also install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface
Convert Roman numerals to integers:

```bash
python main.py XIV
```
Convert integers to Roman numerals:

```bash
python main.py 14 --reverse
```
Validate Roman numerals:

```bash
python main.py XIV --validate
```
Graphical User Interface
Launch the graphical interface:

```bash
python main.py --gui
```
OR
```bash
python gui.py
```

You can also test various Roman numerals by running the script multiple times with different inputs.

## Features

- **Beginner-Friendly**: The code is simple and easy to understand, making it suitable for beginners.
- **Dual Conversion**: Convert both Roman numerals to integers and integers to Roman numerals.
- **Input Validation**: Validate Roman numerals for correctness.
- **Educational**: Learn about Roman numerals and their conversion process.
- **Command-Line Tool**: Easily convert Roman numerals from the command line.
- **Open Source**: Contribute to the project and improve it further.
- **Data Structures**: Understand how to use dictionaries and lists effectively.

## Algorithm

The algorithm used in this project is straightforward. Here’s a brief overview:

1. **Mapping**: Create a mapping of Roman numerals to their integer values.

2. **Iteration**: Iterate through the Roman numeral string from right to left.

3. **Comparison**: If the current numeral is less than the previous numeral, subtract its value. Otherwise, add its value.

4. **Return Result**: After processing the entire string, return the total value.

For integer to Roman conversion:

1. **Value Mapping**: Create lists of integer values and their corresponding Roman symbols.

2. **Iterative Subtraction**: For each value, subtract it from the number as many times as possible, adding the corresponding symbol to the result.

Here is a simple code snippet that illustrates the algorithm:

```python
def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total
```
## Repo Structure
```bash
roman-to-integer-python/
│
├── roman_converter/
│   ├── __init__.py
│   ├── converter.py
│   └── validator.py
│
├── tests/
│   ├── __init__.py
│   └── test_converter.py
│
├── gui.py
├── main.py
├── requirements.txt
└── README.md
```
**roman_converter/**: Package containing core conversion and validation functions

**tests/**: Unit tests for all functionality

**gui.py**: Graphical user interface using Tkinter

**main.py**: Main entry point with multiple usage options

## Contributing

We welcome contributions! If you have ideas for improvements or new features, feel free to submit a pull request. Please ensure your code follows the existing style and includes tests.

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you wish.

## Releases

You can find the latest releases of this project [here](https://github.com/Gabi111243/roman-to-integer-python/releases). Please download the necessary files and execute them as per the instructions provided.

For further updates and information, check the "Releases" section in the repository.

---

Thank you for checking out the **Roman to Integer Converter**! We hope this project helps you understand both Roman numerals and Python programming better. Happy coding!