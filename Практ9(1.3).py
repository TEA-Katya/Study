def reverse_number_recursive(number):
    if number == 0:
        return
    else:
        # Получаем последнюю цифру числа
        last_digit = number % 10
        # Выводим последнюю цифру
        print(last_digit, end="")
        # Рекурсивно вызываем функцию для оставшейся части числа (без последней цифры)
        reverse_number_recursive(number // 10)

# Получаем число от пользователя
try:
    user_input = int(input("Введите целое число: "))
    # Обрабатываем случай отрицательного числа, выводя сначала знак
    if user_input < 0:
        print("-", end="")
        user_input = abs(user_input)

    # Вызываем рекурсивную функцию
    reverse_number_recursive(user_input)
    print() # Добавляем новую строку после вывода числа
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое число.")
