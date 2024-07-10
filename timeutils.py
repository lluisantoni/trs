from typing import List


def day_of_week(year: int, month: int, day: int) -> int:
    # Zeller's Congruence algorithm for calculating day of the week
    month_p = month + (month < 3) * 12
    year_p = year - 1 * (month < 3)
    return (day + 13 * (month_p + 1) // 5
            + year_p + year_p // 4 - year_p // 100
            + year_p // 400) % 7


def is_leap_year(year: int) -> bool:
    if (year % 4 == 0) & ((year % 100 != 0) | (year % 100 == 0 & year % 400 == 0)):
        return True
    return False


def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def date_to_days(date: List[int]) -> int:
    year, month, day = date
    days = day
    for m in range(1, month):
        days += days_in_month(year, m)
    days += (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    return days


def days_between_dates(date1: List[int], date2: List[int]) -> int:
    days1 = date_to_days(date1)
    days2 = date_to_days(date2)
    return abs(days2 - days1)
