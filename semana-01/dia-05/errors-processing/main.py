numbers = []

with open("data.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip()) # convert the line to an integer
            numbers.append(number) # add the number to the list
        except ValueError:
            print(f"Invalid number. Value ignored: {line.strip()}") # print an error message for invalid numbers
print(numbers)