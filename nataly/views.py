from django.shortcuts import render
from .forms import CustomForm
from .wear import get_value_from_5th_column
from .utils import calculation


def index(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные из формы
            product_type = form.cleaned_data['type']
            fabric = form.cleaned_data['fabric']
            size = form.cleaned_data['size']
            element = form.cleaned_data['elements']
            value_from_5th = get_value_from_5th_column(product_type, fabric)
            # Выполняем расчет с использованием value_from_5th
            if value_from_5th is not None:
                calculation_result = calculation(value_from_5th)
            context = {
                'form': form,
                'product_type': product_type,
                'fabric': fabric,
                'size': size,
                'element': element,
                'value_from_5th': value_from_5th,
                'calculation_result': calculation_result,
                'success': True  # Флаг успешной отправки
            }
            return render(request, 'index.html', context)
        else:
            # Если форма невалидна, показываем ошибки
            print('Form errors:', form.errors)
    else:
        form = CustomForm()

    context = {'form': form}
    return render(request, 'index.html', context)


def catalog(request):
    return render(request, 'catalog.html')


def handler404(request, exeption):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
