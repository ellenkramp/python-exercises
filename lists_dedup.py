def single_list(food_list):
  new_list = []
  for item in food_list:
    if item not in new_list:
        new_list.append(item)
  return new_list

food = ['apple', 'cheese', 'apple', 'cheese', 'milk']
print single_list(food)