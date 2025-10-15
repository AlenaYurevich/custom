from django.shortcuts import render
from .forms import CustomForm
from .wear import get_value_from_5th_column, calculation


def index(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные из формы
            # group = form.cleaned_data['group']
            product_type = form.cleaned_data['type']
            fabric = form.cleaned_data['fabric']
            product_size = form.cleaned_data['size']
            product_element = form.cleaned_data['elements']
            value_from_5th = get_value_from_5th_column(product_type, fabric)
            # Выводим для отладки
            # print('Group:', group)
            print('Type:', product_type)
            print('Fabric:', fabric)
            print('Size:', product_size)
            print('Elements:', product_element)
            print('Value from 5th column:', value_from_5th)

            # Выполняем расчет с использованием value_from_5th
            if value_from_5th is not None:
                calculation_result = calculation(value_from_5th)
                # Форматируем цену с разделителями тысяч
                if calculation_result is not None:
                    formatted_price = "{:,.0f}".format(calculation_result).replace(",", " ")
                else:
                    formatted_price = "Ошибка расчета"
            else:
                formatted_price = "Данные не найдены"

            context = {
                'form': form,
                # 'group': group,
                'product_type': product_type,
                'fabric': fabric,
                'product_size': product_size,
                'value_from_5th': value_from_5th,
                'calculation_result': formatted_price,
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


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
