"""Takes an input of year and month

Returns:
    int: Amount of days in year, month
"""

# Determines if the year is a leap year
def isLeapYear(year):
    """Determines if the year is a leap year

    Args:
        year (int): Users inputed year

    Returns:
        Boolean: Returns if year is a leap year
    """    
    if year % 4 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 400 == 0:
        return True
    return False

# Returns the days in month
def days_in_month(year, month):
    """Determine the amount of days in a month. 
        If leap year february is 29 days.

    Args:
        year (int): The users inputed year
        month (int): The users inputed month

    Returns:
        int: The amount of days at the [Year, Month]
    """
    if isLeapYear(year) == False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month-1]
    elif isLeapYear(year) == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month-1]
