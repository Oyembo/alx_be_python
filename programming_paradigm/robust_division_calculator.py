def safe_divide(numerator, denominator):
    safe_divide = numerator / denominator
    return safe_divide
except ZeroDivisionError("Division by zero is not allowed")
    return "Error: Cannot divide by zero."
try:
    numerator = float(numerator)
    denominator = float(denominator)
    result = float(numerator)/ float(denominator)
    return result
except ValueError:
    return "Error: Please enter numeric values only."
    
    