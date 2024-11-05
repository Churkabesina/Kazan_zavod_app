import os
import subprocess

ui_sources_dir = "./ui_sources"
designer_ui_dir = "./designer_UI"

os.makedirs(designer_ui_dir, exist_ok=True)

for filename in os.listdir(ui_sources_dir):
    if filename.endswith(".ui"):
        ui_filepath = os.path.join(ui_sources_dir, filename)

        py_filename = filename[:-3] + "_ui.py"
        py_filepath = os.path.join(designer_ui_dir, py_filename)

        try:
            subprocess.run(["pyside6-uic", ui_filepath, "-o", py_filepath])
            print(f"Успешно сконвертировано: {ui_filepath} -> {py_filepath}")
        except FileNotFoundError:
            print(f"Ошибка: pyside6-uic не найден. Установите PySide6 и добавьте его в PATH.")
        except Exception as e:
            print(f"Ошибка при конвертации {ui_filepath}: {e}")