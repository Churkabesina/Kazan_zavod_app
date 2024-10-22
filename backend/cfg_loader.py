import configparser
import os


def load_cfg() -> configparser.ConfigParser:
    config_file = './config.ini'
    config = configparser.ConfigParser()

    default_config = {
        'DB': {
            'db_path': './db',
            'db_name': 'QSQLITE'
        },
        'Chto-to eshe': {
            'key3': 'value3'
        }
    }

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        config = configparser.ConfigParser()
        for section, options in default_config.items():
            config[section] = options
        with open(config_file, 'w') as f:
            config.write(f)

    for section, options in default_config.items():
        if section not in config:
            config[section] = {}
        for key, value in options.items():
            if key not in config[section]:
                config[section][key] = value

    with open(config_file, 'w') as f:
        config.write(f)

    return config