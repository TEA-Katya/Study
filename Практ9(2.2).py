def find_second_max(current_max, current_second_max):
    try:
        num = int(input("Введите последовательность натуральных чисел по одному (завершите ввод нулем): "))
    except ValueError:
        # Если ввели не число, просто игнорируем и продолжаем с теми же значениями
        return find_second_max(current_max, current_second_max)

    if num == 0:
        #Встречаем 0 - ввод закончен. Возвращаем второе по величине число.
        return current_second_max
    else:
        if num > current_max:
            return find_second_max(num, current_max)
        elif num > current_second_max:
            return find_second_max(current_max, num)
        else:
            return find_second_max(current_max, current_second_max)

#Запускаем рекурсию.(Если первое введенное число будет 5, то max станет 5, а second_max останется 0)
result = find_second_max(0, 0)

print(f"Второе по величине число: ", result)
