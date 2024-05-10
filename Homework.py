# Завдання 1
# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.

import threading
import random
numbers = []

def fill_random_numbers(nums):
    for _ in range(10):
        nums.append(random.randint(1, 100))
    print("Отриманий список:", nums)
def find_sum(nums):
    sum_result = sum(nums)
    print("Сума елементів списку:", sum_result)
def find_average(nums):
    if nums:
        average = sum(nums) / len(nums)
        print("Середнє арифметичне значення у списку:", average)
    else:
        print("Список пустий.")



fill_thread = threading.Thread(target=fill_random_numbers, args=(numbers,))
sum_thread = threading.Thread(target=find_sum, args=(numbers,))
average_thread = threading.Thread(target=find_average, args=(numbers,))
fill_thread.start()
fill_thread.join()
sum_thread.start()
average_thread.start()
sum_thread.join()
average_thread.join()





