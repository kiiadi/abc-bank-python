from datetime import datetime


class DateProvider:
    @staticmethod
    def now():
        return datetime.now()