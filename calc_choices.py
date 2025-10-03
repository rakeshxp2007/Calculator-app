# Addition
def do_addition(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

# Subtraction
def do_subtraction(a: float, b: float) -> float:
    """Subtract second number from first and return the result."""
    return a - b

# Multiplication
def do_multiplication(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

# Division
def do_division(a: float, b: float) -> float:
    """Divide first number by second and return the result."""
    if b == 0:
        raise ValueError("Error! Division by zero.")
    return a / b
    