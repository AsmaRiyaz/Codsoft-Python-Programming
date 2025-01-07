def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    """Main function to perform calculations."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("Select an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation = input("Enter your choice (1/2/3/4): ")

            if operation == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif operation == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif operation == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif operation == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Invalid operation choice. Please try again.")

            another = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another != "yes":
                print("Thank you for using the Simple Calculator! Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
