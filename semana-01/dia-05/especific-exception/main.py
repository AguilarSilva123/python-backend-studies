try:
    input = int(input("Enter a number: "))
    result = 10 / input
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Can not divide by zero!")