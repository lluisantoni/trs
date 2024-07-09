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


def week_days_between_dates_slow(start_date_str, end_date_str):
    if start_date_str > end_date_str:
        start_date_str, end_date_str = end_date_str, start_date_str
    # Convert string dates to datetime objects
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

    # Initialize the count of weekdays
    weekday_count = 0

    # Iterate through the range of dates
    current_date = start_date
    while current_date <= end_date:
        # Check if the current day is a weekday (Monday=0, Sunday=6)
        if current_date.weekday() < 5:
            weekday_count += 1
        # Move to the next day
        current_date += datetime.timedelta(days=1)

    return weekday_count