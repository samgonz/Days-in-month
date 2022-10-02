#Determines if the year is a leap year
def isLeapYear(year):
    if year % 4 == 0:
        return True

    if year % 100 == 0:
        return False
        
    if year % 400 == 0:
        return True
    return False

#Determine the amount of days in a month. 
#If leap year february is 29 days.
def days_in_month(year, month):
    if isLeapYear(year) == False:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        return month_days[month-1]
    elif isLeapYear(year) == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        return month_days[month-1]