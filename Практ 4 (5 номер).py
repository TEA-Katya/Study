def sum_of_cubes(n):

  total_sum = 0
  for i in range(1, n + 1):
    total_sum += i**3
  return total_sum

n = int(input("Введите натуральное число n: "))
result = sum_of_cubes(n)
print(f"Сумма кубов от 1 до {n} равна: {result}")
