from decimal import Decimal
from bs4 import BeautifulSoup


def to_decimal(value: str, precision: int = 2) -> Decimal:

    return round(Decimal(value), precision)


def get_oschadbank(url):
    soup = BeautifulSoup(url.content, 'html.parser')
    al = soup.find_all('td', class_='heading-block-currency-rate__table-col')

    n = len(al)
    rate_list = []
    rate_dict = {}

    for i in range(n):
        rate = soup.find_all('td', class_='heading-block-currency-rate__table-col')[i].get_text()
        rate_list.append(rate)

    for US in rate_list:
        if US == 'USD':
            rate_dict[US] = {
                'Sale': rate_list[rate_list.index(US) + 2],
                'Buy': rate_list[rate_list.index(US) + 3]
            }
        elif US == 'EUR':
            rate_dict[US] = {
                'Sale': rate_list[rate_list.index(US) + 2],
                'Buy': rate_list[rate_list.index(US) + 3]
            }

    return rate_dict


def get_alfabank(url):
    soup = BeautifulSoup(url.content, 'html.parser')
    al = soup.find_all('h4', class_='exchange-rate-tabs__info-value')

    n = len(al)

    rate_list = []
    rate_dict = {}

    for i in range(n):
        rate = soup.find_all('h4', class_='exchange-rate-tabs__info-value')[i].get_text()
        rate_list.append(rate.replace(' ', '').replace('\n', ''))

    rate_list.insert(0, soup.find_all('h3',
                                      class_='exchange-rate-tabs__item-label')[0].get_text().replace(' ', '').replace(
        '\n', ''))
    rate_list.insert(3, soup.find_all('h3',
                                      class_='exchange-rate-tabs__item-label')[1].get_text().replace(' ', '').replace(
        '\n', ''))

    for US in rate_list:
        if US == 'USD':
            rate_dict[US] = {'Sale': rate_list[rate_list.index(US) + 1], 'Buy': rate_list[rate_list.index(US) + 2]}
        elif US == 'EUR':
            rate_dict[US] = {'Sale': rate_list[rate_list.index(US) + 1], 'Buy': rate_list[rate_list.index(US) + 2]}
    return rate_dict


def get_universalbank(url):
    soup = BeautifulSoup(url.content, 'html.parser')
    al = soup.find_all('td')
    n = len(al)

    rate_list = []
    rate_dict = {}

    for i in range(n):
        rate = soup.find_all('td')[i].get_text()
        rate_list.append(rate.replace(' ', '').replace('\n', ''))

    for US in rate_list:
        if US == 'USD':
            rate_dict[US] = {'Buy': rate_list[rate_list.index(US) + 1], 'Sale': rate_list[rate_list.index(US) + 2]}
        elif US == 'EUR':
            rate_dict[US] = {'Buy': rate_list[rate_list.index(US) + 1], 'Sale': rate_list[rate_list.index(US) + 2]}
    return rate_dict
