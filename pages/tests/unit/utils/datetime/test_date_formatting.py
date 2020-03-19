import pytest

from pages.tests.fixtures import utils_fixtures
from pages.utils.datetime import date_formatting


@pytest.mark.parametrize('date, expected', utils_fixtures.date_in_multiple_formats_provider())
def test_if_current_date_is_correct(date, expected):
    formatter = date_formatting.FilenameFormatDateFormatter()
    actual = formatter.format_date(date)

    assert expected == actual
