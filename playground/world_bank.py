import logging

import wbgapi as wb
from pycountry import currencies, countries
from requests import request

BASIC_FORMAT = "%(name)s [%(levelname)s] %(message)s"
logging.basicConfig(format=BASIC_FORMAT, level='INFO')
log = logging.getLogger(__name__)


def price_level_ratio_of_ppp(from_country, to_country):
    """
    Price level ration of Purchasing Power Parity(PPP)
    conversion factor to market exchange rate.
    https://wdi.worldbank.org/table/4.16
    """
    log.info("Fetching PPP ratio of %s(%s)", to_country.name, to_country.alpha_3)
    ppp_to_country = wb.data.get(['PA.NUS.PPPC.RF'], to_country.alpha_3)['value']
    log.info("Fetching PPP ratio of %s(%s)", from_country.name, from_country.alpha_3)
    ppp_from_country = wb.data.get(['PA.NUS.PPPC.RF'], from_country.alpha_3)['value']
    ratio = ppp_to_country / ppp_from_country
    log.info("PPP ratio of %s & %s: %s", to_country.name, from_country.name, ratio)
    return ratio


def convert_amount(from_currency, amount, to_currency):
    """
    Convert the amount based on current market rate

    This method take USA as base unit
    """
    response = request('GET', 'https://api.currencyfreaks.com/latest?apikey=53e0139d6ff040f08e31c7a5b7ca10f9').json()
    rates = response['rates']
    log.info("Fetching currency ratio of %s(%s)", to_currency.name, to_currency.alpha_3)
    to_currency_rate = float(rates[to_currency.alpha_3])
    log.info("Fetching currency ratio of %s(%s)", from_currency.name, from_currency.alpha_3)
    from_currency_rate = float(rates[from_currency.alpha_3])
    ratio = to_currency_rate / from_currency_rate
    log.info("Currency conversation rate of %s & %s: %s", to_currency.name, from_currency.name, ratio)

    return round(ratio * amount, 0)


def string_formatted(country, currency, amount):
    country_string = f'{country.name}({country.alpha_3}){country.flag}'
    currency_string = f'{currency.name}({currency.alpha_3})'
    return f"{country_string}'s {amount:,} {currency_string}"


def search_country_and_currency(country_fuzzy_query: str | tuple | list):
    """
    Perform a fuzzy search on given string.
    It can country code, name or region name.
    """
    log.info("Fuzzy query to find country: %s", country_fuzzy_query)

    if isinstance(country_fuzzy_query, str):
        country = countries.search_fuzzy(country_fuzzy_query)[0]
        currency = currencies.get(numeric=country.numeric)
    elif isinstance(country_fuzzy_query, (tuple, list)):
        country = countries.search_fuzzy(country_fuzzy_query[0])[0]
        currency = currencies.lookup(country_fuzzy_query[1])
    else:
        raise TypeError('Has to be one of str or tuple or list')

    assert country is not None, "Country can't be null"
    log.info("Country found: %s", country)
    assert currency is not None, "Currency can't be null"
    log.info("Currency found: %s", currency)

    return country, currency


def convert(from_country_fuzzy_query: str | tuple | list, amount: float, to_country_fuzzy_query: str | tuple | list):
    from_country, from_currency = search_country_and_currency(from_country_fuzzy_query)
    to_country, to_currency = search_country_and_currency(to_country_fuzzy_query)

    ratio = price_level_ratio_of_ppp(from_country, to_country)

    final_amount = amount * ratio
    converted_final_amount = convert_amount(from_currency, final_amount, to_currency)

    print(string_formatted(from_country, from_currency, amount))
    print("is")
    print(string_formatted(to_country, to_currency, converted_final_amount))


def main():
    convert('India', 3000000, ('Germany', 'Euro'))


if __name__ == '__main__':
    main()
