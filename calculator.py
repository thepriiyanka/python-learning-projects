import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def power(x, y):
    return math.pow(x, y)

def square(x):
    return x * x

def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    return math.sqrt(x)

def cube(x):
    return x ** 3

def cube_root(x):
    if x < 0:
        return "Error! Cannot take cube root of a negative number."
    return x ** (1/3)

def factorial(x):
    return math.factorial(int(x))

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm only works for positive numbers."
    return math.log10(x)

def trigonometry(x):
    rad = math.radians(x)
    return math.sin(rad), math.cos(rad), math.tan(rad)

def display_menu():
    print("\n====== SIMPLE CALCULATOR (MULTI-FUNCTION) ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Cube")
    print("10. Cube Root")
    print("11. Factorial")
    print("12. Logarithm (base 10)")
    print("13. Trigonometry (sin, cos, tan)")
    print("14. Exit")

def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "14":
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Operations requiring two numbers
            if choice in ["1", "2", "3", "4", "5", "6"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Addition: {addition(num1, num2)}")
                elif choice == "2":
                    print(f"Subtraction: {subtraction(num1, num2)}")
                elif choice == "3":
                    print(f"Multiplication: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Division: {division(num1, num2)}")
                elif choice == "5":
                    print(f"Modulus: {modulus(num1, num2)}")
                elif choice == "6":
                    print(f"Power: {power(num1, num2)}")

            # Operations requiring one number
            elif choice in ["7", "8", "9", "10", "11", "12"]:
                num = int(input("Enter a number: "))

                if choice == "7":
                    print(f"Square: {square(num)}")
                elif choice == "8":
                    print(f"Square Root: {square_root(num)}")
                elif choice == "9":
                    print(f"Cube: {cube(num)}")
                elif choice == "10":
                    print(f"Cube Root: {cube_root(num)}")
                elif choice == "11":
                    print(f"Factorial: {factorial(num)}")
                elif choice == "12":
                    print(f"Logarithm (base 10): {logarithm(num)}")

            # Trigonometry
            elif choice == "13":
                angle = float(input("Enter angle in degrees: "))
                sin_val, cos_val, tan_val = trigonometry(angle)
                print("Sin:", sin_val)
                print("Cos:", cos_val)
                print("Tan:", tan_val)

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Error! Invalid input. Please enter numeric values.")
        except Exception as e:
            print("Unexpected Error:", e)

if __name__ == "__main__":
    main()
