def find_duplicates(input_list):
    seen = set() 
    duplicates = set() #Создаем объект-множество
    for item in input_list:
        if item in seen:
            duplicates.add(item) #Добавляем повторно встречающуюся цифру к дубликатам
        seen.add(item) #Добавляем все цифры в увиденные 
    return list(duplicates)

my_list = input("Введите цифры без пробела")
duplicate_elements = find_duplicates(my_list)
print(f"Повторяющиеся элементы: {duplicate_elements}")
