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


def get_choices_for_group(group_id):
    """Возвращает варианты выбора для конкретной группы"""
    if group_id not in sheets:
        return []

    worksheet = sheets[group_id]
    rows = worksheet.max_row
    choices = []
    for i in range(6, rows + 1):
        cell = worksheet.cell(row=i, column=1)
        # Убираем лишние пробелы и проверяем, что значение не пустое
        cleaned_value = str(cell.value).strip()
        if cleaned_value:
            row = (str(i), cleaned_value)  # преобразуем в строку для JSON
            choices.append(row)

    return choices
