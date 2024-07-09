import logging
import datetime
from weekdays import week_days_between_dates
from timeutils import week_days_between_dates_slow

if __name__ == '__main__':
    logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s", level=logging.INFO)

    sd = datetime.date(2024, 1, 1)
    days = 250
    dates = [(sd + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]

    for start_date in dates:
        for en_date in dates:
            slow_value = week_days_between_dates_slow(start_date, en_date)
            fast_value = week_days_between_dates(start_date, en_date)
            if slow_value != fast_value:
                raise Exception(f"Wrong values for {start_date} - {en_date}: expected {slow_value} and actual {fast_value}")


