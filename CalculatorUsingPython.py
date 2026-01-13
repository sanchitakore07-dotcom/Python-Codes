
while True:
    try:
        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Sorry you closed the calculator!!")
            break

        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            print("Result:", num1 / num2)

        else:
            print("Invalid Choice! Select choice between 1 to 5.")

    except ValueError:
        print("Please enter numbers only!")

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    except Exception as e:
        print("Something went wrong:", e)
