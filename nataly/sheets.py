import os
from openpyxl import load_workbook


def load_excel_sheet(file_name):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'files/{file_name}')
    workbook = load_workbook(filename=file_path)
    return workbook.active


# Словарь для хранения ссылок на листы
sheets = {
    1: load_excel_sheet('outerwear.xlsx'),  # Мужская и женская верхняя одежда
    2: load_excel_sheet('women_clothing.xlsx'),  # Женская легкая одежда
    3: load_excel_sheet('men_clothing.xlsx'),  # Мужская легкая одежда
    4: load_excel_sheet('outerwear.xlsx'),  # Детская верхняя одежда (может потребоваться другой файл)
    5: load_excel_sheet('women_clothing.xlsx'),  # Легкая одежда для девочек
    6: load_excel_sheet('men_clothing.xlsx'),  # Легкая одежда для мальчиков
}
