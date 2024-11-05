import configparser
import os
import shutil
from datetime import datetime

import fitz
import xlsxwriter


def load_cfg() -> configparser.ConfigParser:
    config_file = './config.ini'
    config = configparser.ConfigParser()

    default_config = {
        'DB': {
            'db_folder': './db',
            'db_name': 'QSQLITE'
        },
        'PATHS': {
            'draws_folder': './чертежи',
            'export_pdf_folder': './выгрузка PDF',
            'storage_excel_export_path': './склад EXCEL'
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

def create_storage_excel_folder(storage_excel_path: str) -> str:
    if not os.path.exists(storage_excel_path):
        os.makedirs(storage_excel_path)
    return storage_excel_path

def create_temp_products_pdf_folder(temp_products_pdf_path: str) -> str:
    if not os.path.exists(temp_products_pdf_path):
        os.makedirs(temp_products_pdf_path)
    return temp_products_pdf_path

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

def unload_storage_to_excel(storage_excel_export_path: str, data: list[list]):
    folder_path = os.path.abspath(storage_excel_export_path)
    current_date = datetime.today().strftime('%Y-%m-%d')
    filename = 'склад_' + current_date + '.xlsx'
    full_path = os.path.join(folder_path, filename)
    workbook = xlsxwriter.Workbook(full_path)
    worksheet = workbook.add_worksheet()

    for row_num, row_data in enumerate(data):
        for col_num, value in enumerate(row_data):
            worksheet.write(row_num, col_num, value)
    workbook.close()

def unload_products_temp_table_to_pdf(input_paths: list, output_path):
    filename = 'выгрузка_' + datetime.today().strftime('%Y-%m-%d') + '.pdf'
    output_path = os.path.join(os.path.abspath(output_path), filename)
    base_name, ext = os.path.splitext(output_path)
    counter = 1
    final_output_path = output_path

    while os.path.exists(final_output_path):
        final_output_path = f"{base_name}_{counter}{ext}"
        counter += 1
    try:
        result_pdf = fitz.open()
        for pdf_path in input_paths:
            with fitz.open(pdf_path) as src_pdf:
                result_pdf.insert_pdf(src_pdf)
        result_pdf.save(final_output_path)
        print(f"PDF файлы успешно объединены в {final_output_path}")

    except FileNotFoundError:
        print(f"Ошибка: Один или несколько входных файлов не найдены.")
    except Exception as e:
        print(f"Ошибка при объединении PDF: {e}")