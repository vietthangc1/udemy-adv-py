from typing import List
from datetime import datetime
from .flatmate import Flatmate
import calendar

class Bill:
    """
    Contains information about monthly Bill,
    including amount, period in days
    """
    def __init__(self, amount: int, flatmates: List[Flatmate], period = "Dec 2020") -> None:
        self.amount = amount
        self.flatmates = flatmates
        self.period = period
        
        self.total_days = self.calc_total_days()
        self.amt_per_days = self.amount / self.total_days
        self.days = self.month_days()

    def calc_total_days(self) -> int:
        total_days = 0
        for flatmate in self.flatmates:
            total_days += flatmate.days
        return total_days

    def calculate(self, flatmate: Flatmate) -> float:
        return self.amt_per_days * flatmate.days
        
    def month_days(self) -> int:
        period_parsed = datetime.strptime(self.period, "%b %Y")
        month = period_parsed.month
        year = period_parsed.year
        return calendar.monthrange(year, month)[1]


