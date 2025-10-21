import os
from openpyxl import load_workbook
from django.core.cache import cache


def load_excel_sheet(file_name):
    """
    Загружает данные из всех листов с кэшированием
    """
    cache_key = 'excel_data'
    data = cache.get(cache_key)

    if not data:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'files/{file_name}')
        workbook = load_workbook(filename=file_path)
        data = {
            'main_sheet': workbook['Table 1'],
            'elements_sheet': workbook['Table 2'],
        }
        cache.set(cache_key, data, 3600)  # Кэш на 1 час
    return data


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
    # Загружаем данные из кэша
    excel_data = load_excel_sheet('wear.xlsx')
    worksheet = excel_data['main_sheet']  # Используем main_sheet из кэша

    rows = worksheet.max_row
    current_product_type = None
    fabric_str = str(fabric).strip()

    # Определяем, нужно ли применять коэффициент 1.2
    apply_coefficient = (fabric_str == '0')
    # Если тип ткани 0, ищем значение для типа ткани 1
    search_fabric = '1' if apply_coefficient else fabric_str

    for i in range(3, rows + 1):
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
                if fabric_matches(search_fabric, fabric_value_str):
                    value_5th_cell = worksheet.cell(row=i, column=5).value
                    if value_5th_cell is not None:
                        try:
                            value_str = str(value_5th_cell).replace(',', '.')
                            base_value = float(value_str)
                            # Применяем коэффициент 1.2 для типа ткани 0
                            if apply_coefficient:
                                return base_value * 1.2
                            else:
                                return base_value
                        except (ValueError, TypeError):
                            return 0
    return 0


def get_choices_type():
    """
    Получает типы продуктов из кэшированного листа Table 1
    """
    excel_data = load_excel_sheet('wear.xlsx')
    if not excel_data:
        return ()
    main_sheet = excel_data['main_sheet']  # Table 1
    return read_types(main_sheet)


def get_elements_type():
    """
    Получает список элементов из кэшированного листа Table 2
    """
    excel_data = load_excel_sheet('wear.xlsx')
    if not excel_data:
        return ()
    elements_sheet = excel_data['elements_sheet']  # Table 2
    return read_types(elements_sheet)


# Использование
Choices_type = get_choices_type()    # Типы из Table 1
Elements_type = get_elements_type()   # Элементы из Table 2
