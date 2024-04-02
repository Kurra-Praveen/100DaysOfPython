def leapYear(year):
    """
    :param year: takes year as an input
    :return: True if it is leap year else False
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


def daysInMonth(year, month):
    """
    :param year:year as input -->int type
    :param month: months as input --> int type
    :return: the no of days in a month
    """
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapYear(year) and month == 2:
        return 29

    return monthDays[month - 1]


year = int(input("enter the year"))
month = int(input("enter the month"))
days = daysInMonth(year, month)
print(days)

