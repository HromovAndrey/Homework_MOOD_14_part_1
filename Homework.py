# Завдання 4
# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом
# і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу
# із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.

import os
import threading


source_dir = input("Введіть шлях до директорії: ")
search_word = input("Введіть слово для пошуку: ")
banned_words_file = input("Введіть шлях до файлу зі збороненими словами: ")
def search_and_merge_files(source_dir, search_word, output_file):
    try:
        matching_files = []
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        if search_word in file.read():
                            matching_files.append(file_path)
        with open(output_file, 'w') as out_file:
            for file_path in matching_files:
                with open(file_path, 'r') as in_file:
                    out_file.write(in_file.read() + '\n')

        print(f"Знайдено та злито {len(matching_files)} файлів з потрібним словом.")
    except Exception as e:
        print(f"Під час пошуку та злиття файлів виникла помилка: {e}")

def exclude_banned_words(input_file, banned_words_file, output_file):
    try:

        with open(banned_words_file, 'r') as file:
            banned_words = set(file.read().splitlines())

        with open(input_file, 'r') as in_file:
            content = in_file.read()
        for banned_word in banned_words:
            content = content.replace(banned_word, '')

        with open(output_file, 'w') as out_file:
            out_file.write(content)

        print(f"Видалено заборонені слова з файлу {input_file}.")
    except Exception as e:
        print(f"Під час виключення заборонених слів виникла помилка: {e}")


merged_file = 'merged_files.txt'
modified_file = 'modified_file.txt'
search_thread = threading.Thread(target=search_and_merge_files, args=(source_dir, search_word, merged_file))
search_thread.start()
search_thread.join()
exclude_thread = threading.Thread(target=exclude_banned_words, args=(merged_file, banned_words_file, modified_file))
exclude_thread.start()
exclude_thread.join()
print("Операції завершено.")