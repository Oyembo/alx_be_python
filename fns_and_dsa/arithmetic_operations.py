def perform_operation (num1: float, num2: float, operation: str):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
