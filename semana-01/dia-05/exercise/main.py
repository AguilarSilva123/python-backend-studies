numbers = []

with open("data.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Invalid number. Value ignored: {line.strip()}")

sum = sum(numbers)
average = sum / len(numbers) if numbers else 0 # calculate the average, avoiding division by zero
print(numbers)
print(f"Sum: {sum}")
print(f"Average: {average}")