def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the arithmetic operation if successful.
        str: A specific error message "Error: Cannot divide by zero!" if division by zero is attempted.

    Raises:
        ValueError: If an invalid operation string is provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        # Raise a ValueError for unsupported operations
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', 'divide'.")
