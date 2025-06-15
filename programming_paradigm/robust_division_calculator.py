def safe_divide(numerator, denominator):
    ""'Returns division of two values"""
    if denominator > 0:
        result = numerator / denominator
        return result
    elif denominator == 0:
        raise ZeroDivisionError ("Division by zero is not allowed")
    return "Division by zero is not allowed"

try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
        return "Division by zero is not allowed"
        except ValueError:
            return "Please enter numeric values only"
    