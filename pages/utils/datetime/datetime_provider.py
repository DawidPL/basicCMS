import pytz
from datetime import datetime

from pages.utils.datetime.date_formatting import FilenameFormatDateFormatter, IDateFormatter

'''
Raises UnknownTimeZoneError if passed an unknown timezone.
'''


class DatetimeAsStringProvider:
    def now(self, date_formatter: IDateFormatter = FilenameFormatDateFormatter(),
            timezone: str = "Europe/Warsaw") -> str:
        date = datetime.now(pytz.timezone(timezone))
        if date_formatter:
            date = date_formatter.format_date(date)
        return date
