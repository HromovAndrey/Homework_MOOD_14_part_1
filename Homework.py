# Завдання 3
# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран

import os
import threading
source_dir = input("Введіть шлях до існуючої директорії: ")
dest_dir = input("Введіть шлях до нової директорії: ")


def copy_directory_contents(source_dir, dest_dir):
    try:

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)


        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)
            if os.path.isdir(source_item):
                copy_directory_contents(source_item, dest_item)
            else:
                with open(source_item, 'rb') as source_file:
                    with open(dest_item, 'wb') as dest_file:
                        dest_file.write(source_file.read())

        print(f"Директорія {source_dir} успішно скопійована в {dest_dir}")
    except Exception as e:
        print(f"Під час копіювання виникла помилка: {e}")


copy_thread = threading.Thread(target=copy_directory_contents, args=(source_dir, dest_dir))
copy_thread.start()
copy_thread.join()
print("Копіювання завершено.")




