from unittest.mock import MagicMock, patch

from app.currency.tasks import parse_monobank, parse_privatbank, parse_vkurse, parse_oschadbank, \
    parse_alfabank, parse_universalbank

from currency.models import Rate


def test_parse_monobank(mocker):
    response_json = [
        {"currencyCodeA": 820, "currencyCodeB": 980, "date": 1664572209, "rateBuy": 36.65, "rateSell": 37.9507},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1664572209, "rateBuy": 35.65, "rateSell": 37.4504},
        {"currencyCodeA": 978, "currencyCodeB": 840, "date": 1664572209, "rateBuy": 0.965, "rateSell": 0.985}
    ]
    initial_rate_count = Rate.objects.count()
    _ = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_json)
    )
    assert Rate.objects.count() == initial_rate_count
    parse_monobank()


def test_parse_privatbank(mocker):
    response_json = [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "1111.56860", "sale": "37.45318"},
        {"ccy": "ww", "base_ccy": "UAH", "buy": "34.92000", "sale": "37.45318"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "18530.5432", "sale": "20481.1266"}
    ]
    initial_rate_count = Rate.objects.count()

    _ = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_json),
    )
    assert Rate.objects.count() == initial_rate_count
    parse_privatbank()


def test_parse_vkurse(mocker):
    response_json = {
        "w": {"buy": "22.30", "sale": "11.85"}, "Euro": {"buy": "66.70", "sale": "55.30"},
    }
    _ = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda:
                               response_json),
    )

    parse_vkurse()


@patch('app.currency.tasks.get_oschadbank')
def test_parse_oschadbank(mock_get, mocker):
    _ = mocker.patch('requests.get')
    response_json = {
        "w": {"Sale": "33.4000", "Buy": "33.9500"}, "EUR": {"Sale": "33.6000", "Buy": "33.6000"},
    }
    mock_get.return_value = response_json
    parse_oschadbank()


@patch('app.currency.tasks.get_alfabank')
def test_parse_alfabank(mock_get, mocker):
    response_link = 'https://alfabank.ua/currency-exchange'
    _ = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: response_link)
    )
    response_json = {
        "w": {"Sale": "33.4000", "Buy": "33.9500"}, "EUR": {"Sale": "33.6000", "Buy": "33.6000"},
    }
    mock_get.return_value = response_json
    parse_alfabank()


@patch('app.currency.tasks.get_universalbank')
def test_parse_universalbank(mock_get, mocker):
    _ = mocker.patch('requests.get', )
    response_json = {
        "sdf": {"Sale": "33.4000", "Buy": "33.9500"}, "EUR": {"Sale": "12.6000", "Buy": "33.6000"}
    }

    mock_get.return_value = response_json
    parse_universalbank()
