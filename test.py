import logging
from weekdays import week_days_between_dates
from timeutils import week_days_between_dates_slow

if __name__ == '__main__':
    logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s", level=logging.INFO)

    dates = ["2024-06-01", "2024-06-02", "2024-06-03", "2024-06-04", "2024-06-05", "2024-06-06", "2024-06-07",
             "2024-06-08", "2024-06-09", "2024-06-10", "2024-06-11", "2024-06-12", "2024-06-13", "2024-06-14",
             "2024-06-15", "2024-06-16", "2024-06-17", "2024-06-18", "2024-06-19", "2024-06-20", "2024-06-21"]

    for start_date in dates:
        for en_date in dates:
            slow_value = week_days_between_dates_slow(start_date, en_date)
            fast_value = week_days_between_dates(start_date, en_date)
            if slow_value != fast_value:
                raise Exception(f"Wrong values for {start_date} - {en_date}: expected {slow_value} and actual {fast_value}")


