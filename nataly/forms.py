from django import forms
from .wear import Choices_type, Elements_type


Choices_fabric = [(5, f'Тип ткани'),
                  (0, f'0 - Шелковый бархат на шелковой и х/б основе, вельвет синт.'),
                  (1, f'1 - Натуральные: шелк, кожа, замша, х/б бархат, трикотаж с ворсовой поверх.'),
                  (2, f'2 - Шерсть, в т.ч с содерж. синтетических волокон, иск. мех, иск. кожа, иск. замша,'
                      f' трикотаж, х/б кружево, х/б вельвет'),
                  (3, f'3 - Хлопок, лен: пальтовые, костюмные ткани, махровая ткань'),
                  (4, f'4 - Хлопок, лен: плательные, сорочечные и корсетные ткани и аналогичные по сложности обработки')
                  ]


Choices_size = [(0, f'Размер'),
                (1, f'Взрослый'),
                (2, f'Детский'),
                # (3, f'30-34'),
                # (4, f'36-40'),
                # (5, f'40-44'),
                ]


class CustomForm(forms.Form):
    type = forms.TypedChoiceField(
        choices=Choices_type,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-1 text-wrap",
            'autofocus': 'autofocus',
            'aria-label': "Default select example",
        })
    )
    fabric = forms.TypedChoiceField(
        choices=Choices_fabric,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-1 text-wrap",
            'aria-label': "Default select example",
        })
    )
    size = forms.TypedChoiceField(
        choices=Choices_size,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-1 text-wrap",
            'aria-label': "Default select example",
        })
    )
    elements = forms.TypedChoiceField(
        choices=Elements_type,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-1 text-wrap",
            'aria-label': "Default select example",
        })
    )
