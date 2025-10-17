from django import forms
from .wear import read_types, Choices_type


# Choices_group = [(0, f'Группа изделий'),
#                  (1, f'Мужская и женская верхняя одежда'),
#                  (2, f'Женская легкая одежда '),
#                  (3, f'Мужская легкая одежда'),
#                  (4, f'Детская верхняя одежда'),
#                  (5, f'Легкая одежда для девочек'),
#                  (6, f'Легкая одежда для мальчиков'),
#                  ]


# Choices_type = [(0, f'Тип изделия'),
#                 (1, f'Пальто, полупальто зимние (с подкладкой, в т.ч. из иск. меха, и утепляющей прокладкой)'),
#                 (2, f'Жакет зимний (с подкладкой в т.ч. из искусственного меха и утепляющей прокладкой)'),
#                 (3, f'Пальто, полупальто демисезонные, летние, плащ (с подкладкой)'),
#                 (4, f'Пальто, полупальто летние, плащ (без подкладки)'),
#                 (5, f'Пиждак (с подкладкой)'),
#                 (6, f'Пиждак (без подкладки)'),
#                 (7, f'Жакет (с подкладкой)'),
#                 (8, f'Жакет (без подкладки)'),
#                 ]
# def read_types(worksheet):
#     rows = sheet.max_row
#     choices = []
#     for i in range(3, rows + 1):
#         cell = worksheet.cell(row=i, column=1)
#         if cell.value is not None and str(cell.value).strip() != '':
#             choice = (cell.value, cell.value)  # (значение для бэкенда, отображаемое значение)
#             choices.append(choice)
#     choices = tuple(choices)
#     return choices


Choices_fabric = [(0, f'Тип ткани'),
                  (1, f'1'),
                  (2, f'2'),
                  (3, f'3'),
                  (4, f'4'),
                  ]


Choices_size = [(0, f'Размер'),
                (1, f'Взрослый'),
                # (2, f'Детский:'),
                # (3, f'30-34'),
                # (4, f'36-40'),
                # (5, f'40-44'),
                ]


Choices_element = [(0, f'Усложняющие элементы'),
                   (1, f'нет'),
                   (2, f' 1 ед.'),
                   (3, f' 2 ед.'),
                   (4, f' 3 ед.'),
                   ]


class CustomForm(forms.Form):
    type = forms.TypedChoiceField(
        choices=Choices_type,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2 text-wrap",
            'autofocus': 'autofocus',
            'aria-label': "Default select example",
            'placeholder': "111",
        })
    )
    fabric = forms.TypedChoiceField(
        choices=Choices_fabric,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2 text-wrap",
            'aria-label': "Default select example",
        })
    )
    size = forms.TypedChoiceField(
        choices=Choices_size,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2 text-wrap",
            'aria-label': "Default select example",
        })
    )
    elements = forms.TypedChoiceField(
        choices=Choices_element,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2 text-wrap",
            'aria-label': "Default select example",
        })
    )
