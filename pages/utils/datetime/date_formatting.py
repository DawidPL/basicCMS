from abc import ABCMeta, abstractmethod
from datetime import datetime


class IDateFormatter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def format_date(self, date_to_format: datetime) -> str: raise NotImplementedError


class FilenameFormatDateFormatter(IDateFormatter):

    def format_date(self, date_to_format: datetime) -> str:
        return date_to_format.strftime('%Y-%m-%d_%H-%M-%S')
