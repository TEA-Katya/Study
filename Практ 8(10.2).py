def sort_columns_by_row(matrix, k_idx):
    if not matrix:
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if not (0 <= k_idx < num_rows):
        print(f"Индекс строки k_idx  ({k_idx})выходит за пределы допустимого диапазона. Он должен быть в диапазоне от 0 до {num_rows - 1}.")
        return matrix

    col_value_pairs = [(matrix[k_idx][j], j) for j in range(num_cols)]
    col_value_pairs.sort()
    sorted_col_indices = [pair[1] for pair in col_value_pairs]

    sorted_matrix = [[matrix[i][j] for j in sorted_col_indices] for i in range(num_rows)]
    return sorted_matrix

def get_matrix_from_user():
    while True:
        try:
            rows = int(input("Введите количество строк (M): "))
            if rows <= 0:
                print("Количество строк должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    while True:
        try:
            cols = int(input("Введите количество столбцов (N): "))
            if cols <= 0:
                print("Количество столбцов должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    matrix = []
    print(f"Введите элементы матрицы ({rows}x{cols}).")
    print("Каждую строку вводите, разделяя элементы пробелом.")

    for i in range(rows):
        while True:
            row_input = input(f"Строка {i + 1}: ")
            try:
                row_elements = list(map(int, row_input.split()))
                if len(row_elements) != cols:
                    print(f"Ошибка: Введено {len(row_elements)} элементов, а ожидалось {cols}. Попробуйте снова.")
                else:
                    matrix.append(row_elements)
                    break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, вводите только целые числа, разделенные пробелом.")
    return matrix


user_matrix = get_matrix_from_user()

if not user_matrix:
    print("Матрица не была введена.")
else:
    num_rows_user = len(user_matrix)
    
    while True:
        try:
            k_row_problem_idx = int(input(f"Введите номер строки (k), по которой нужно отсортировать столбцы (от 1 до {num_rows_user}): "))
            k_idx_for_function = k_row_problem_idx - 1
            
            if not (0 <= k_idx_for_function < num_rows_user):
                print(f"Ошибка: Номер строки должен быть в диапазоне от 1 до {num_rows_user}.")
            else:
                break 
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    print("\nИсходная матрица:")
    for row in user_matrix:
        print(row)

    sorted_user_matrix = sort_columns_by_row(user_matrix, k_idx_for_function)

    print(f"\nМатрица с отсортированными столбцами по строке {k_row_problem_idx} (индекс {k_idx_for_function}):")
    for row in sorted_user_matrix:
        print(row)
