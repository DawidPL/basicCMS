import pytest
from datetime import datetime


def date_in_multiple_formats_provider():
    date = [datetime.strptime('2018-05-20 11:23:44.09867', '%Y-%m-%d %H:%M:%S.%f'),
            datetime.strptime('2019-12-01 09:01:22', '%Y-%m-%d %H:%M:%S'),
            datetime.strptime('2020-01-05', '%Y-%m-%d')]
    expected = ['2018-05-20_11-23-44', '2019-12-01_09-01-22', '2020-01-05_00-00-00']
    zip_list = [(d1, d2) for d1, d2 in zip(date, expected)]
    return zip_list
