from django.shortcuts import render
from .forms import CustomForm
from django.http import JsonResponse
from django.views import View
from .sheets import get_choices_for_group


class GetProductTypesView(View):
    def get(self, request, *args, **kwargs):  # Убрать @staticmethod
        group_id = request.GET.get('group_id')

        if not group_id:
            return JsonResponse({'error': 'Group ID is required'}, status=400)

        try:
            group_id = int(group_id)
            choices = get_choices_for_group(group_id)
            return JsonResponse({'types': choices})
        except (ValueError, KeyError) as e:
            print(f"Error in GetProductTypesView: {e}")  # Логирование для отладки
            return JsonResponse({'error': 'Invalid group ID'}, status=400)


def index(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            # Получаем очищенные данные из формы
            group = form.cleaned_data['group']
            product_type = form.cleaned_data['type']

            # Выводим для отладки
            print('Group:', group)
            print('Type:', product_type)

            # Здесь обычно сохраняем в базу или обрабатываем данные
            # Например:
            # product = Product(group=group, type=product_type)
            # product.save()

            context = {
                'form': form,
                'group': group,
                'product_type': product_type,
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
