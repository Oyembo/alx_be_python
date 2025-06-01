num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case addition: 
    addition = num1 + num2
        print("addition") #Print The result is [addition]
    case subtraction:
    subtraction = num1 - num2
        print("The result is "[subtraction]"") #Print The result is [subtraction]
    case multiplication:
    multiplication = num1 * num2
        print("The result is "[multiplication]"") #Print The result is [multiplication]
    case division:
    division = num1 / num2
        print("The result is "[division]"") #Print The result is [division]
    case _:
        print("Cannot divide by zero") #Print The result is [not available]


    
