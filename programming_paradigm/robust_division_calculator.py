def safe_divide(numerator, denominator):
    """Performs division and handle any errors"""
    result = numerator / denominator
    return result
try:
    numerator = float(numerator)
    denominator = float(denominator)
    result = float(numerator)/ float(denominator)
    return result
except ZeroDivisionError("Division by zero is not allowed")
    return "Error: Cannot divide by zero."
except ValueError:
    return "Error: Please enter numeric values only."
    
    