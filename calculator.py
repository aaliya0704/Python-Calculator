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


def main():
    print("=" * 30)
    print("Welcome to python calculator")
    print("=" * 30)

    num1 = get_number()
    num2 = get_number()
    print("Addition: ", add((num1, num2)))
    print("subtraction: ", subtract(num1, num2))
    print("Division: ", divide(num1, num2))
    print("Multiplication: ", multiply(num1, num2))


if __name__ == "__main__":
    main()
