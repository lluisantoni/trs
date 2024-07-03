import logging
from timeutils import day_of_week, days_between_dates


def week_days_between_dates(date1: str, date2: str):
    date1 = [int(i) for i in date1.split('-')]
    date2 = [int(i) for i in date2.split('-')]
    number_of_days = days_between_dates(date1, date2)
    full_weeks = number_of_days // 7
    week_days_within = full_weeks * 5
    day_of_week_1 = day_of_week(date1[0], date1[1], date1[2])
    day_of_week_2 = day_of_week(date2[0], date2[1], date2[2])
    week_days = (week_days_within + \
                ((day_of_week_2 - day_of_week_1) % 7) + 1
                 - 1 * (day_of_week_1 < 2) - 1 * (day_of_week_2 < 2))
    return week_days


if __name__ == '__main__':
    logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s", level=logging.INFO)

    start_date = "2010-06-01"
    end_date = "2023-06-30"
    logging.info(f"There are {week_days_between_dates(start_date, end_date)} weekdays.")
