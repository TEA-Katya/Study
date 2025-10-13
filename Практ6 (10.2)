import random

def process_array():
    # Создаем массив из 15 случайных элементов от 0 до 30
    arr = [random.randint(0, 30) for _ in range(15)]
    print("Одномерный массив:", arr)

    # Создаем измененный массив
    modified_arr = []
    for element in arr:
        if element < 10:
            modified_arr.append(0)
        elif element > 20:
            modified_arr.append(1)
        else:
            modified_arr.append(element)

    print("Измененный массив:", modified_arr)

process_array()
