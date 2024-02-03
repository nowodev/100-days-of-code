def is_leap(year):
    """
    Checks if the year is a leap year
    :param year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    Returns the number of days in a given month, for a given year / leap year
    :param year:
    :param month:
    :return:
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return month_days[month - 1] + 1

    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
