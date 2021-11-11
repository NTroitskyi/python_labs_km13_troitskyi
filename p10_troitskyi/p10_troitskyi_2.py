import numpy as np

years = np.arange(1900, 2020+1, 1)

def leap_year(x):
    new_years = list(filter(lambda i: i % 400 != 0 and i % 100 == 0, x))
    res = list(set(years) - set(new_years))
    res = list(filter(lambda i: i % 4 == 0, res))
    return res

while True:
    while True:
        try:
            year = int(input('Enter a year from 1900 to 2020: '))
        except Exception as error:
            print(error)
            continue
        else:
            break
    if year not in range(1900, 2020+1):
        print('Number of year is not in range from 1900 to 2020. Try again.')
        continue
    while True:
        try:
            month = int(input('Enter a month from 1 to 12: '))
        except Exception as error:
            print(error)
            continue
        else:
            break
    if month not in range(1, 12+1):
        print('Number of month is not in range from 1 to 12. Try again.')
        continue
    break

def days_number(func, month, year):
    if year in func:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: 
            return 'There are 31 days in this month'
        elif month == 2:
            return'There are 29 days in this month'
        else:
            return 'There are 30 days in this month'
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 'There are 31 days in this month'
        elif month == 2:
            return'There are 28 days in this month'
        else:
            return'There are 30 days in this month'




    

print('Years: \n',years)
print('Leap years: \n',leap_year(years))
print(days_number(leap_year(years), month, year))