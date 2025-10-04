#Division
def do_division(a: float, b: float) -> float:
    """Divide first number by second and return the result."""
    if b == 0:
        raise ValueError("Error! Division by zero.")
    return a / b