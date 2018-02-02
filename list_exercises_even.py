def even(numbers):
  length = len(numbers)
  new_num = []
  for i in range(0,(length-1)):
    if (numbers[i]%2) == 0:
      new_num.append(numbers[i])
  return new_num

numbers = [1, 2, 3, 4, 6, 7, 9]
print even(numbers)