from decimal import Decimal, ROUND_HALF_UP
from .models import SiteSettings


def calculation(value_from_5th, value_for_element):
    """
    Рассчитывает стоимость пошива одного изделия на основе настроек сайта.

    Args:
        value_from_5th (float): Норма времени на раскрой и пошив в часах.

    Returns:
        dict: Словарь со всеми промежуточными расчетами и итоговой стоимостью.
    """

    # Получаем единственный объект настроек сайта
    # Если объекта нет, используем значения по умолчанию (create_defaults=False)
    settings = SiteSettings.load()

    # Формат для округления до 2 знаков
    TWO_PLACES = Decimal('0.01')
    TEN_ROUBLES = Decimal('10')  # до 10 рублей

    # Конвертируем целочисленные поля в Decimal для точных расчетов
    avg_salary = Decimal(settings.average_salary_per_month)
    working_hours = Decimal(settings.working_hours_per_month)
    equipment_cost = Decimal(settings.equipment_cost)
    equipment_lifespan = Decimal(settings.equipment_lifespan_months)

    # Расчет часовой ставки
    salary_per_hour = (avg_salary / working_hours).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # Расчет амортизации оборудования в месяц
    equipment_depreciation_per_month = (equipment_cost / equipment_lifespan).quantize(TWO_PLACES,
                                                                                      rounding=ROUND_HALF_UP)

    # Суммарные месячные затраты (без учета зарплаты и налога на нее)
    total_monthly_costs = (
            settings.rent_per_month +
            settings.utilities_per_month +
            equipment_depreciation_per_month +
            settings.materials_per_month +
            settings.advertising_per_month
    )

    # Расчет затрат в час (на аренду, комуналки, амортизацию, материалы и рекламу)
    costs_per_hour = (total_monthly_costs / working_hours).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # РАСЧЕТ СЕБЕСТОИМОСТИ ИЗДЕЛИЯ
    # Заработная плата на изделие
    salary_per_item = (salary_per_hour * Decimal(value_from_5th + value_for_element)).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # Налог на профессиональный доход с зарплаты за изделие
    professional_tax = (salary_per_item * (settings.professional_income_tax / Decimal(100))).quantize(TWO_PLACES,
                                                                                                      rounding=ROUND_HALF_UP)

    # Накладные расходы за время пошива изделия
    overhead_costs = (costs_per_hour * Decimal(value_from_5th + value_for_element)).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # Полная себестоимость изделия
    cost_price = (salary_per_item + professional_tax + overhead_costs).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # РАСЧЕТ ИТОГОВОЙ ЦЕНЫ
    # Прибыль (15%)
    profit_margin = (cost_price * Decimal(0.15)).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # Итоговая цена до округления
    final_price_before_rounding = (cost_price + profit_margin).quantize(TWO_PLACES, rounding=ROUND_HALF_UP)

    # Округление до целого числа (математическое округление)
    final_price_rounded = (final_price_before_rounding / TEN_ROUBLES).quantize(Decimal('1.'),
                                                                               rounding=ROUND_HALF_UP) * TEN_ROUBLES

    # Формируем детализированный результат
    result = {
        'settings': settings,
        'input_hours': value_from_5th,

        # Промежуточные расчеты
        'salary_per_hour': salary_per_hour,
        'equipment_depreciation_per_month': equipment_depreciation_per_month,
        'total_monthly_costs': total_monthly_costs,
        'costs_per_hour': costs_per_hour,

        # Расчет себестоимости изделия
        'salary_per_item': salary_per_item,
        'professional_tax': professional_tax,
        'overhead_costs': overhead_costs,
        'cost_price': cost_price,

        # Итоговая цена
        'profit_margin': profit_margin,
        'final_price_before_rounding': final_price_before_rounding,
        'final_price_rounded': final_price_rounded,
    }
    print('норма времени', value_from_5th, 'ЗП в час', salary_per_hour)
    print('норма времени для элемента', value_for_element)
    print('аморитизация в месяц', equipment_depreciation_per_month)
    print('затраты в месяц', total_monthly_costs, 'накладные расходы в час', costs_per_hour)
    print('ЗП на изделие', salary_per_item)
    print('налог 10%', professional_tax, 'накладные расходы', overhead_costs)
    print('себестоимость', cost_price, 'прибыль, руб.', profit_margin)
    print('цена до округления', final_price_before_rounding, 'цена после округления', final_price_rounded)
    return result
