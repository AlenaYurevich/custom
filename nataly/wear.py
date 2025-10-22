import os
from openpyxl import load_workbook


def load_excel_sheet(file_name):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'files/{file_name}')
    workbook = load_workbook(filename=file_path)
    return workbook.active


worksheet = load_excel_sheet('wear.xlsx')  # одежда


def read_types(wearsheet):
    rows = wearsheet.max_row
    choices = []
    for i in range(3, rows + 1):
        cell = wearsheet.cell(row=i, column=1)
        if cell.value is not None and str(cell.value).strip() != '':
            choices.append((cell.value, cell.value))
    return tuple(choices)


def get_value_from_5th_column(product_type, fabric):
    """
    Возвращает значение из 5-й колонки для указанного типа продукта и ткани
    """
    rows = worksheet.max_row
    for i in range(3, rows + 1):
        cell_value = worksheet.cell(row=i, column=1).value
        # Сравниваем значения, учитывая возможные различия в форматировании
        if cell_value is not None and str(cell_value).strip() == str(product_type).strip():
            if fabric == '1':
                value_3th = str(worksheet.cell(row=i, column=3).value)
                if value_3th == fabric:
                    # Получаем значение из 5-й колонки (column=5)
                    value_5th = float(worksheet.cell(row=i, column=5).value)
            elif fabric == '2':
                value_5th = float(worksheet.cell(row=i + 1, column=5).value)
            elif fabric == '3':
                value_5th = float(worksheet.cell(row=i + 2, column=5).value)
            return value_5th
    return None  # Если не нашли соответствие


Choices_type = read_types(worksheet)


def calculation(value_from_5th):

    return value_from_5th * 2
