def sort_columns(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            M, N, k = map(int, f_in.readline().split())

            if not (1 <= k <= M):
                raise ValueError(f"ОЗначение k ({k}) должно быть в диапазоне от 1 до M ({M}).")

            matrix = []
            for _ in range(M):
                row = list(map(int, f_in.readline().split()))
                if len(row) != N:
                    raise ValueError(f"Количество столбцов не совпадает. Нужно {N}, получено {len(row)}.")
                matrix.append(row)

        #Сортируем столбцы
        columns_as_rows = list(zip(*matrix))
        sorted_columns_as_rows = sorted(columns_as_rows, key=lambda col: col[k - 1])
        sorted_matrix = list(map(list, zip(*sorted_columns_as_rows)))

        #Выодим в файл
        with open(output_file, 'w') as f_out:
            for row in sorted_matrix:
                f_out.write(" ".join(map(str, row)) + '\n')

        print(f"Матрица отсортирована и сохранена в '{output_file_path}'.")

    except FileNotFoundError:
        print(f"файл не найден.")
    except ValueError as e:
        print(f"Ошибка в формате или значении: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

input_file = "C:\\Users\\User\\Desktop\\TerekhovaEA_UB-51_vvod.txt"
output_file = "C:\\Users\\User\\Desktop\\TerekhovaEA_UB-51_vivod.txt"

sort_columns(input_file, output_file)
