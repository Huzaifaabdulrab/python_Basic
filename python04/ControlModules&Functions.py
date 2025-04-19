# Import custom module with alias m_d
import math_module as m_d

# Function to check even or odd number
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Call the function
check_even_odd(7)


# Simple calculator function
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid Operator"

# Call the calculator
print(calculator(10, 5, '+'))  # Output: 15


# Using functions from custom module
print(m_d.add(10, 5))       # Using add function from math_module
print(m_d.multiply(4, 3))   # Using multiply function from math_module
