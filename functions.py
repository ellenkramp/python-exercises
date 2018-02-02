
# def sum(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
    
# print sum([1, 2, 3, 4])

def multiply(a, b):
    listc = []
    for i in range(len(a)):
      listc.append(a[i] * b[i])
    return listc

lista = [2, 4, 6]
listb = [1, 3, 5]

print multiply(lista, listb)