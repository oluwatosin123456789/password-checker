def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        # Get user inputs
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please input +, -, *, or /.")
            return

        # Display result
        print(f"The result is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()