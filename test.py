import logging
import datetime
from weekdays import week_days_between_dates


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


if __name__ == '__main__':
    logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s", level=logging.INFO)

    sd = datetime.date(399, 1, 1)
    days = 250 * 4
    dates = [(sd + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, days, 5)]

    for start_d in dates:
        for end_d in dates:
            slow_value = week_days_between_dates_slow(start_d, end_d)
            fast_value = week_days_between_dates(start_d, end_d)
            if slow_value != fast_value:
                raise Exception(f"Wrong values for {start_d} - {end_d}: expected {slow_value} and actual {fast_value}")


