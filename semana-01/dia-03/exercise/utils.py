def calculate_average(numbers):
    quantity = len(numbers)
    sum = 0 
    for number in numbers:
        sum = number + sum
    average =  sum/quantity
    return average