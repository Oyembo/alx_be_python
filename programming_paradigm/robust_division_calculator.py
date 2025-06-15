def safe_divide(numerator, denominator):
    """Returns division of two values"""
    if denominator > 0:
        result = numerator / denominator
        return result
    elif denominator == 0:
        raise ZeroDivisionError ("Division by zero is not allowed")
    return "Error: Cannot divide by zero."

try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
        return "Error: Cannot divide by zero."
        except ValueError:
            return "Error: Please enter numeric values only."
    