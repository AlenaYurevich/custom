from django import forms


Choices_group = [(0, f'Группа изделий'),
                 (1, f'Мужская и женская верхняя одежда'),
                 (2, f'Женская легкая одежда '),
                 (3, f'Мужская легкая одежда'),
                 (4, f'Детская верхняя одежда'),
                 (5, f'Легкая одежда для девочек'),
                 (6, f'Легкая одежда для мальчиков'),
                 ]


class CustomForm(forms.Form):
    group = forms.TypedChoiceField(
        choices=Choices_group,
        initial=0,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2",
            'autofocus': 'autofocus',
            'aria-label': "Default select example",
            'id': 'id_group'  # добавляем ID для JavaScript
        })
    )

    type = forms.TypedChoiceField(
        choices=[],  # изначально пустой
        required=False,
        widget=forms.Select(attrs={
            'class': "form-select border-0 py-2",
            'aria-label': "Default select example",
            'id': 'id_type',
            'disabled': 'disabled'  # изначально выключено
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Изначально поле type пустое
        self.fields['type'].choices = []
