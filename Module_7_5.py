import os
import time

current_path = os.getcwd()  # Текущая директория

for root, dirs, files in os.walk(current_path):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.basename(root)

        print(f'Обнаружен файл: {file}\n'
              f' Путь: {filepath}\n'
              f' Родительская директория: {parent_dir}\n'
              f' Время изменения: {formatted_time}\n'
              f' Размер: {file_size} байт\n')
