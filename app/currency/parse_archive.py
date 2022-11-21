import requests
from datetime import *
from app.currency.models import Rate, Source
from app.currency import consts
from app.currency import model_choices as mch
from app.currency.utils import to_decimal


def parse_archive_privatbank():
    from currency.models import Rate, Source
    #changing date type
    str_date = '20.10.2022'
    start_date = datetime.strptime(str_date, "%d.%m.%Y").date()
    current_date = date.today()

    while start_date != current_date:
        if Rate.objects.filter(created=start_date).count():
            start_date += timedelta(days=1)
            continue

        url = f'''https://api.privatbank.ua/p24api/
        exchange_rates?json&date={start_date.day}.{start_date.month}.{start_date.year}'''

        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()

        currency_type_mapper = {
            'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
            'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
            'EUR': mch.CurrencyType.CURRENCY_TYPE_UER,
            'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC,
        }

        source = Source.objects.get_or_create(
            code_name=consts.CODE_NAME_PRIVATBANK,
            defaults={'url': url, 'name': 'PrivatBank'}
        )[0]

        for rate_data in response_data['exchangeRate']:
            try:
                currency_type = rate_data['currency']
                base_currency_type = rate_data['baseCurrency']
            except KeyError:
                continue
            if currency_type == base_currency_type:
                continue
            if currency_type not in currency_type_mapper or \
                    base_currency_type not in currency_type_mapper:
                continue

            currency_type = currency_type_mapper[rate_data['currency']]
            base_currency_type = currency_type_mapper[rate_data['baseCurrency']]

            buy = to_decimal(rate_data['purchaseRateNB'])
            sale = to_decimal(rate_data['saleRateNB'])

            try:
                latest_rate = Rate.objects.filter(
                    currency_type=currency_type,
                    base_currency_type=base_currency_type,
                    source=source,
                    created=start_date
                ).latest('created')
            except Rate.DoesNotExist:
                latest_rate = None

            if latest_rate is None or \
                    latest_rate.sale != sale or \
                    latest_rate.buy != buy:
                Rate.objects.create(
                    base_currency_type=base_currency_type,
                    currency_type=currency_type,
                    buy=buy,
                    sale=sale,
                    source=source,
                    created=start_date,
                )
        start_date += timedelta(days=1)
