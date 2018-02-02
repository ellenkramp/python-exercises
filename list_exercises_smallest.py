
def smallest(numbers):
  numbers.sort()
  length = len(numbers)
  return numbers[0]

numbers = [1, 2, 3, 4, 6, 7, 9]

print smallest(numbers)