from django import forms
from .wear import Choices_type


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
