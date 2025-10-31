import random
    
def numbers_of_segment():
    a, b, c = input("a: "), input("b: "), input("c: ")
    N = random.randint(210,231)

    count = 0
    # Проходимся по всем числам на отрезке от 100 до N
    for num in range(100, N + 1):
        # Преобразуем число в строку для проверки цифр
        num_str = str(num)
        
        # Проверяем, состоит ли число только из заданных цифр
        is_composed_of_allowed_numbers = True  #состоит из разрешенных цифр
        for digit in num_str:
            if digit not in (a, b, c):
                is_composed_of_allowed_numbers = False
                break
        
        # Если число состоит только из разрешенных цифр, увеличиваем счетчик
        if is_composed_of_allowed_numbers:
            count += 1

    print(f"Количество чисел, составленных из цифр {a}, {b}, {c} на отрезке [100, {N}]: {count}")

numbers_of_segment()
