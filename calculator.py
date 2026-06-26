def get_number():
    number = float(input("enter a number: "))
    return number


def main():
    print("=" * 30)
    print("Welcome to python calculator")
    print("=" * 30)

    num1 = get_number()
    num2 = get_number()
    print(num1)
    print(num2)


if __name__ == "__main__":
    main()
