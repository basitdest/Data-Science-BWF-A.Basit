while True:
    try:
        num1 = int(input("Enter the first number (or 'q' to quit): "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is {result}.")
    except ValueError:
        print("Please enter valid numbers.")
    if input("Would you like to perform another calculation? (yes/no): ").lower() != 'yes':
        break
