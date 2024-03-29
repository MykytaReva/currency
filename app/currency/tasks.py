from celery import shared_task
from django.core.mail import send_mail

from django.core.cache import cache
from settings import settings

import requests
from datetime import datetime, date, timedelta

from currency.utils import to_decimal, get_oschadbank,\
    get_alfabank, get_universalbank

from currency import consts
from currency import model_choices as mch


@shared_task
def send_email_contact_us(subject, message, email_to):
    email_subject = subject
    message_to = message
    email_to_to = email_to

    send_mail(
        email_subject,
        message_to,
        settings.EMAIL_HOST_USER,
        [email_to_to],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

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

    for rate_data in response_data:
        currency_type = rate_data['ccy']
        base_currency_type = rate_data['base_ccy']

        # skip unsupported curencies
        if currency_type not in currency_type_mapper or \
                base_currency_type not in currency_type_mapper:
            continue

        currency_type = currency_type_mapper[rate_data['ccy']]
        base_currency_type = currency_type_mapper[rate_data['base_ccy']]

        buy = to_decimal(rate_data['buy'])
        sale = to_decimal(rate_data['sale'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )
            cache.clear()
            # cache.set()


@shared_task
def parse_archive_privatbank():
    from currency.models import Rate, Source

    str_date = '17.10.2022'
    start_date = datetime.strptime(str_date, "%d.%m.%Y").date()
    current_date = date.today()

    while start_date != current_date:

        if Rate.objects.filter(created=start_date).count():
            start_date += timedelta(days=1)
            continue

        url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + \
            f'{start_date.day}.{start_date.month}.{start_date.year}'

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


@shared_task
def parse_monobank():
    from currency.models import Rate, Source
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()

    currency_type_mapper = {
        980: mch.CurrencyType.CURRENCY_TYPE_UAH,
        840: mch.CurrencyType.CURRENCY_TYPE_USD,
        978: mch.CurrencyType.CURRENCY_TYPE_UER,
    }
    source = Source.objects.get_or_create(
         code_name=consts.CODE_NAME_MONOBANK,
         defaults={'url': url, 'name': 'MonoBank'}
    )[0]

    for rate_data in response_data:
        currency_type = rate_data['currencyCodeA']
        base_currency_type = rate_data['currencyCodeB']

        if currency_type not in currency_type_mapper or \
                base_currency_type not in currency_type_mapper:
            continue

        currency_type = currency_type_mapper[rate_data['currencyCodeA']]
        base_currency_type = currency_type_mapper[rate_data['currencyCodeB']]

        buy = to_decimal(rate_data['rateBuy'])
        sale = to_decimal(rate_data['rateSell'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )


@shared_task
def parse_vkurse():
    from currency.models import Rate, Source
    link = 'http://vkurse.dp.ua'
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()

    currency_type_mapper = {
        'Dollar': mch.CurrencyType.CURRENCY_TYPE_USD,
        'Euro': mch.CurrencyType.CURRENCY_TYPE_UER,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_VKURSE,
        defaults={'url': link, 'name': 'Vkurse'}
    )[0]

    for rate_data in response_data:
        currency_type = rate_data
        base_currency_type = mch.CurrencyType.CURRENCY_TYPE_UAH

        if currency_type not in currency_type_mapper:
            continue

        buy = to_decimal(response_data[rate_data]['buy'])
        sale = to_decimal(response_data[rate_data]['sale'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )


@shared_task
def parse_oschadbank():
    from currency.models import Source, Rate

    link = 'https://www.oschadbank.ua/currency-rate'
    url = requests.get(link)

    rate_oschad = get_oschadbank(url)

    currency_type_mapper = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_UER,
    }
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_OSCHADBANK,
        defaults={'url': link, 'name': 'OschadBank'}
    )[0]

    for rate_data in rate_oschad:
        currency_type = rate_data
        base_currency_type = mch.CurrencyType.CURRENCY_TYPE_UAH

        if currency_type not in currency_type_mapper:
            continue

        buy = to_decimal(rate_oschad[rate_data]['Buy'])
        sale = to_decimal(rate_oschad[rate_data]['Sale'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )


@shared_task
def parse_alfabank():
    from currency.models import Rate, Source

    link = 'https://alfabank.ua/currency-exchange'
    url = requests.get(link)

    rate_alfabank = get_alfabank(url)
    # breakpoint()
    currency_type_mapper = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_UER,
    }

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_ALFABANK,
        defaults={'url': link, 'name': 'AlfaBank'}
    )[0]

    for rate_data in rate_alfabank:
        currency_type = rate_data
        base_currency_type = mch.CurrencyType.CURRENCY_TYPE_UAH

        if currency_type not in currency_type_mapper:
            continue

        buy = to_decimal(rate_alfabank[rate_data]['Buy'])
        sale = to_decimal(rate_alfabank[rate_data]['Sale'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )


@shared_task
def parse_universalbank():
    from currency.models import Rate, Source

    link = 'https://www.universalbank.com.ua/'
    url = requests.get(link)

    rate_universalbank = get_universalbank(url)

    currency_type_mapper = {
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_UER,
    }
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_UNIVERSALBANK,
        defaults={'url': link, 'name': 'UniversalBank'}
    )[0]

    for rate_data in rate_universalbank:
        currency_type = rate_data
        base_currency_type = mch.CurrencyType.CURRENCY_TYPE_UAH

        if currency_type not in currency_type_mapper:
            continue

        buy = to_decimal(rate_universalbank[rate_data]['Buy'])
        sale = to_decimal(rate_universalbank[rate_data]['Sale'])

        try:
            latest_rate = Rate.objects.filter(
                currency_type=currency_type,
                base_currency_type=base_currency_type,
                source=source
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
            )
