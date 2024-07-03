import datetime
from typing import List


def day_of_week(year: int, month: int, day: int) -> int:
    # Zeller's Congruence algorithm for calculating day of the week
    if month < 3:
        month += 12
        year -= 1
    return (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7


def days_between_dates(date1: List[int], date2: List[int]) -> int:
    m = datetime.datetime(date1[0], date1[1], date1[2])
    n = datetime.datetime(date2[0], date2[1], date2[2])
    return abs((n-m).days)
