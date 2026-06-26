def get_number():
    number = float(input("enter a number: "))
    return number


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def menu_display():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")


def main():
    print("=" * 30)
    print("Welcome to python calculator")
    print("=" * 30)
# Displying the menu
menu_display()
    num1 = get_number()
    num2 = get_number()
    print("Addition: ", add((num1, num2)))
    print("subtraction: ", subtract(num1, num2))
    print("Division: ", divide(num1, num2))
    print("Multiplication: ", multiply(num1, num2))


if __name__ == "__main__":
    main()
