def get_number():
    number = float(input("enter a number: "))
    return number


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by 0")
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
    while True:
        menu_display()
        choice = input("Enter your choice [1, 2, 3, 4, 5]: ")
        if choice == "5":
            print("Thankyou for using the calculator!")
            break
        elif choice in ["1", "2", "3", "4"]:
            num1 = get_number()
            num2 = get_number()

            if choice == "1":
                result = add(num1, num2)
                print(result)

            elif choice == "2":
                result = subtract(num1, num2)
                print(result)

            elif choice == "3":
                try:
                    result = divide(num1, num2)
                    print(result)
                except ZeroDivisionError as error:
                    print("Error", error)

            elif choice == "4":
                result = multiply(num1, num2)
                print(result)
        else:
            print("invalid number, make sure you select a number between 1 - 5")


if __name__ == "__main__":
    main()
