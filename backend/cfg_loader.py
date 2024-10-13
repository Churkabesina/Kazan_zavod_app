import configparser
import os


def load_cfg() -> configparser.ConfigParser:
    config_file = './config.ini'
    config = configparser.ConfigParser()

    # Стандартные настройки
    default_config = {
        'PATHS': {
            'db_path': './db',
        },
        'Section2': {
            'key3': 'value3'
        }
    }

    # Проверяем, существует ли файл конфигурации
    if os.path.exists(config_file):
        # Если файл существует, читаем его
        config.read(config_file)
    else:
        # Если файла нет, создаем его с дефолтными настройками
        config = configparser.ConfigParser()
        for section, options in default_config.items():
            config[section] = options
        with open(config_file, 'w') as f:
            config.write(f)

    # Проверяем наличие секций и ключей, добавляем недостающие
    for section, options in default_config.items():
        if section not in config:
            config[section] = {}
        for key, value in options.items():
            if key not in config[section]:
                config[section][key] = value

    # Сохраняем изменения в файле (если были)
    with open(config_file, 'w') as f:
        config.write(f)

    return config