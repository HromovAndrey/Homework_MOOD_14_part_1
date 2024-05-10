# Завдання 2
# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.

import threading
import random
import math

def fill_file_with_random_numbers(file_path):
    with open(file_path, 'w') as file:
        for _ in range(10):
            file.write(str(random.randint(1, 100)) + '\n')

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(file_path):
    primes = []
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            if is_prime(number):
                primes.append(number)
    return primes

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def find_factorials(file_path):
    factorials = []
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorials.append(factorial(number))
    return factorials

def main():

    file_path = input("Введіть шлях до файлу: ")
    fill_thread = threading.Thread(target=fill_file_with_random_numbers, args=(file_path,))
    fill_thread.start()
    fill_thread.join()
    primes_thread = threading.Thread(target=find_primes, args=(file_path,))
    factorials_thread = threading.Thread(target=find_factorials, args=(file_path,))
    primes_thread.start()
    factorials_thread.start()
    primes_thread.join()
    factorials_thread.join()
    primes = primes_thread.result()
    factorials = factorials_thread.result()
    with open("primes.txt", 'w') as primes_file:
        for prime in primes:
            primes_file.write(str(prime) + '\n')

    with open("factorials.txt", 'w') as factorials_file:
        for factorial_num in factorials:
            factorials_file.write(str(factorial_num) + '\n')

    print("Кількість знайдених простих чисел:", len(primes))
    print("Кількість обчислених факторіалів:", len(factorials))

if __name__ == "__main__":
    main()