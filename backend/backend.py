import configparser
import os
import shutil
import sys


def load_cfg() -> configparser.ConfigParser:
    config_file = './config.ini'
    config = configparser.ConfigParser()

    default_config = {
        'DB': {
            'db_path': './db',
            'db_name': 'QSQLITE'
        },
        'DRAWS': {
            'draws_folder': './чертежи'
        }
    }

    if os.path.exists(config_file):
        config.read(config_file, encoding='UTF-8')
    else:
        config = configparser.ConfigParser()
        for section, options in default_config.items():
            config[section] = options
        with open(config_file, 'w', encoding='UTF-8') as f:
            config.write(f)

    for section, options in default_config.items():
        if section not in config:
            config[section] = {}
        for key, value in options.items():
            if key not in config[section]:
                config[section][key] = value

    with open(config_file, 'w', encoding='UTF-8') as f:
        config.write(f)

    return config

def create_draws_folder(folder_path: str) -> str:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def copy_pdf_to_draws_folder(source_path: str, destination_path: str):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{os.path.basename(source_path)}' успешно скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except PermissionError:
        print(f"Ошибка: Недостаточно прав для копирования в '{destination_path}'.")
    except Exception as e:
        print(f"Произошла ошибка при копировании: {e}")