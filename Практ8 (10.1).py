def is_sorted(row):
    #Проверяем, отсортирован ли список по возрастанию или убыванию
    if len(row) <= 1:
        return True

    increasing = all(row[i] <= row[i+1] for i in range(len(row)-1))
    decreasing = all(row[i] >= row[i+1] for i in range(len(row)-1))

    return increasing or decreasing

def find_max_in_sorted_rows(matrix):
    #Находим максимальный элемент в упорядоченных строках матрицы
    max_value = float('-inf')  # Инициализируем минимальным возможным значением
    for row in matrix:
        if is_sorted(row):
            max_value = max(max_value, max(row))
    if max_value == float('-inf'):
        return None #Если нет упорядоченных строк
    return max_value

def input_matrix():
    #Ввод матрицы пользователем
    rows = int(input("Введите количество строк в матрице: "))
    cols = int(input("Введите количество столбцов в матрице: "))
    matrix = []

    for i in range(rows):
        while True:
            try:
                row_str = input(f"Введите элементы упорядоченной строки через пробел {i + 1}: ")
                row = [float(x) for x in row_str.split()]  # Разделяем строку на числа
                if len(row) == cols:
                    matrix.append(row)
                    break #Переходим к следующей строке, если ввод неправильный
                else:
                    print(f"Ошибка: Введите ровно {cols} элемента(ов) для строки.")
            except ValueError:
                print("Ошибка: Некорректный ввод. Введите числа через пробел.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")

    return matrix

matrix = input_matrix()
max_value = find_max_in_sorted_rows(matrix)

if max_value is not None:
    print("Максимальный элемент в упорядоченных строках:", max_value)
else:
    print("В матрице нет упорядоченных строк."
