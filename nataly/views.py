from django.shortcuts import render
from .forms import CustomForm


def index(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные из формы
            group = form.cleaned_data['group']
            product_type = form.cleaned_data['type']
            product_fabric = form.cleaned_data['fabric']
            product_size = form.cleaned_data['size']
            product_element = form.cleaned_data['elements']
            # Выводим для отладки
            print('Group:', group)
            print('Type:', product_type)
            print('Fabric:', product_fabric)
            print('Size:', product_size)
            print('Elements:', product_element)

            # Здесь обычно сохраняем в базу или обрабатываем данные
            # Например:
            # product = Product(group=group, type=product_type)
            # product.save()

            context = {
                'form': form,
                'group': group,
                'product_type': product_type,
                'product_fabric': product_fabric,
                'product_size': product_size,

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
