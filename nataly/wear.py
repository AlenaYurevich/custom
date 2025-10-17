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
    Универсальная версия с улучшенной обработкой диапазонов ткани
    """
    rows = worksheet.max_row
    current_product_type = None
    fabric_str = str(fabric).strip()

    for i in range(3, rows + 1):
        # Получаем значение из первой колонки
        cell_value = worksheet.cell(row=i, column=1).value

        # Если в первой колонке есть значение - это новый product_type
        if cell_value is not None and str(cell_value).strip():
            current_product_type = str(cell_value).strip()

        # Пропускаем строки, если еще не нашли нужный product_type
        if current_product_type is None:
            continue

        # Проверяем, совпадает ли текущий product_type с искомым
        if current_product_type == str(product_type).strip():
            # Получаем значение ткани из 2-й колонки
            fabric_value = worksheet.cell(row=i, column=2).value

            if fabric_value is not None:
                fabric_value_str = str(fabric_value).strip()

                # Функция для проверки совпадения ткани
                def fabric_matches(input_fabric, table_fabric):
                    input_fabric = str(input_fabric).strip()
                    table_fabric = str(table_fabric).strip()

                    # Точное совпадение
                    if input_fabric == table_fabric:
                        return True

                    # Проверка диапазонов типа "3-4"
                    if '-' in table_fabric:
                        try:
                            start, end = map(str.strip, table_fabric.split('-'))
                            start_num, end_num = int(start), int(end)
                            input_num = int(input_fabric)
                            return start_num <= input_num <= end_num
                        except (ValueError, IndexError):
                            return False

                    return False

                # Проверяем совпадение с использованием функции
                if fabric_matches(fabric_str, fabric_value_str):
                    value_5th_cell = worksheet.cell(row=i, column=5).value
                    if value_5th_cell is not None:
                        try:
                            value_str = str(value_5th_cell).replace(',', '.')
                            return float(value_str)
                        except (ValueError, TypeError):
                            return 0
    return 0


Choices_type = read_types(worksheet)


def calculation(value_from_5th):
    return value_from_5th * 2
