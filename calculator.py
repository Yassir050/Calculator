import math

history = []

def calculate(num1, operator, num2=None):
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    elif operator == "%":
        return num1 % num2

    elif operator == "**":
        return num1 ** num2

    elif operator == "sqrt":
        if num1 < 0:
            return "Error: Cannot calculate square root of a negative number"
        return math.sqrt(num1)

    else:
        return "Error: Invalid operator"


while True:
    print("\n========================")
    print("      CALCULATOR")
    print("========================")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Modulo         (%)")
    print("6. Power          (**)")
    print("7. Square Root    (sqrt)")
    print("8. History")
    print("9. Exit")

    choice = input("\nChoose an option: ")

    if choice == "9":
        print("Calculator closed.")
        break

    elif choice == "8":
        print("\n--- History ---")

        if not history:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

        continue

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid option.")
        continue

    try:
        num1 = float(input("Enter first number: "))

        if choice == "7":
            result = calculate(num1, "sqrt")
            operation = f"√{num1} = {result}"

        else:
            operators = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/",
                "5": "%",
                "6": "**"
            }

            operator = operators[choice]
            num2 = float(input("Enter second number: "))

            result = calculate(num1, operator, num2)
            operation = f"{num1} {operator} {num2} = {result}"

        print("\nResult:", result)

        if not isinstance(result, str):
            history.append(operation)

    except ValueError:
        print("Error: Please enter valid numbers.")
