def summation(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

numbers = [1, 2, 3, 4, 6, 7, 9]
print summation(numbers)