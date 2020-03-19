import pytest
from unittest import mock

from pages.utils.datetime.date_formatting import IDateFormatter
from pages.utils.datetime.datetime_provider import DatetimeAsStringProvider


def test_now_raises_error_on_invalid_timezone_string():
    from pytz import UnknownTimeZoneError
    with pytest.raises(UnknownTimeZoneError):
        datetime_provider = DatetimeAsStringProvider()
        datetime_provider.now(timezone='some_invalid_string')


def test_now_returns_date_in_valid_format():
    expected = '2020-04-20'
    date_formatter = mock.Mock(IDateFormatter)
    date_formatter.format_date.return_value = expected
    datetime_provider = DatetimeAsStringProvider()

    actual = datetime_provider.now(date_formatter)

    assert expected == actual


def test_now_returns_date_from_valid_timezone():
    date_formatter = mock.Mock(IDateFormatter)
    date_formatter.format_date.side_effect = lambda date: date  # Funkcja "format_date" zwraca podaną datę bez zmian
    datetime_provider = DatetimeAsStringProvider()

    warsaw_timezone_date = datetime_provider.now(date_formatter, 'Europe/Warsaw')
    gmt_timezone_date = datetime_provider.now(date_formatter, 'GMT')

    assert warsaw_timezone_date.strftime('%Z') == 'CET'
    assert gmt_timezone_date.strftime('%Z') == 'GMT'
    assert warsaw_timezone_date.strftime('%T') != gmt_timezone_date.strftime('%T')
