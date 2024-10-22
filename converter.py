import os
import subprocess

# Пути к папкам с .ui файлами и сгенерированным кодом
ui_sources_dir = "./ui_sources"
designer_ui_dir = "./designer_UI"

# Создаем папку для сгенерированных файлов, если её нет
os.makedirs(designer_ui_dir, exist_ok=True)

# Находим все .ui файлы в папке ui_sources_dir
for filename in os.listdir(ui_sources_dir):
    if filename.endswith(".ui"):
        # Полный путь к .ui файлу
        ui_filepath = os.path.join(ui_sources_dir, filename)

        # Формируем имя для .py файла
        py_filename = filename[:-3] + "_ui.py"
        py_filepath = os.path.join(designer_ui_dir, py_filename)

        # Выполняем команду pyside6-uic для конвертации
        try:
            subprocess.run(["pyside6-uic", ui_filepath, "-o", py_filepath])
            print(f"Успешно сконвертировано: {ui_filepath} -> {py_filepath}")
        except FileNotFoundError:
            print(f"Ошибка: pyside6-uic не найден. Установите PySide6 и добавьте его в PATH.")
        except Exception as e:
            print(f"Ошибка при конвертации {ui_filepath}: {e}")