numbers = [2, 3, 5, 8, 12]

squared = [n**2 for n in numbers] # raise each of the numbers to the power of 2

print(squared)

evens = [n for n in numbers if n % 2 == 0] # only evens numbers

print(evens)