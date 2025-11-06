def is_prime(n):
    #Проверяет, является ли число простым.
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_binary_palindrome(n):
    #Проверяем, является ли двоичная запись числа палиндромом.
    binary = bin(n)[2:] # Получаем двоичную запись
    return binary == binary[::-1]

def find_binary_numbers(n_limit):
    #Находит все простые числа, не превосходящие n_limit, чья двоичная запись - палиндром.
    return [n for n in range(2, n_limit + 1) if is_prime(n) and is_binary_palindrome(n)]


n = int(input("Задайте верхнюю границу: " ))
result = find_binary_numbers(n)
print(f"Простые числа до {n}, двоичная запись которых - палиндром: {res
