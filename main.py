import calculateDaysInMonth

#Gathers the users year and month
year = int(input('Enter in a year.'))
month = int(input('Enter the month number (Ex: December would be [12])'))

#Determines the amount of days at the inputed year and month
days_month = calculateDaysInMonth.days_in_month(year, month)

print(f'{days_month}')