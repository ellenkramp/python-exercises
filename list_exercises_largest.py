def largest(arr):
  arr.sort()
  length = len(arr)
  return arr[(length-1)]

numbers = [1, 2, 3, 4, 10, 7, 9]

print largest(numbers)