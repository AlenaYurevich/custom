import logging
from django.shortcuts import render
from .forms import CustomForm
from .wear import get_value_from_table1, get_value_for_element
from .utils import calculation


logger = logging.getLogger(__name__)


def index(request):
    """
    Главная страница с формой расчета
    """
    context = {'form': CustomForm()}

    if request.method != "POST":
        return render(request, 'index.html', context)

    # Обработка POST-запроса
    form = CustomForm(request.POST)

    if not form.is_valid():
        logger.warning(f'Форма невалидна: {form.errors}')
        context['form'] = form
        return render(request, 'index.html', context)

    try:
        # Получаем очищенные данные из формы
        cleaned_data = form.cleaned_data
        product_type = cleaned_data['type']
        fabric = cleaned_data['fabric']
        size = cleaned_data['size']
        element = cleaned_data['elements']

        # Получаем значения из таблиц
        value_from_5th = get_value_from_table1(product_type, fabric)
        value_for_element = get_value_for_element(element, fabric)

        # Выполняем расчет
        calculation_result = None
        if value_from_5th is not None and value_for_element is not None:
            calculation_result = calculation(value_from_5th, value_for_element)

        # Подготавливаем контекст
        context.update({
            'form': form,
            'product_type': product_type,
            'fabric': fabric,
            'size': size,
            'element': element,
            'value_from_5th': value_from_5th,
            'value_for_element': value_for_element,
            'calculation_result': calculation_result,
            'success': True
        })

        # Логирование успешного расчета
        logger.info(
            f"Успешный расчет: тип={product_type}, ткань={fabric}, "
            f"элемент={element}, результат={calculation_result}"
        )

    except Exception as e:
        logger.error(f'Ошибка при обработке формы: {e}', exc_info=True)
        context['error'] = 'Произошла ошибка при расчете. Попробуйте еще раз.'
        context['success'] = False

    return render(request, 'index.html', context)


def catalog(request):
    return render(request, 'catalog.html')


def handler404(request, exeption):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
