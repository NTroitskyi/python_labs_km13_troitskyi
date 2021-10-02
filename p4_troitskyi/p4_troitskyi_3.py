import math
while True:
    minutes1 = input('How many minutes spent: ')
    try:
        minutes = float(minutes1)
    except ValueError:
        print('This is not a number. Try again')
        continue
    if (0 <= minutes <= 50):
        print('It costs 100 hrn')
        break
    elif (50 < minutes < 100):
        print('It costs 150 hrn')
        break
    elif (minutes > 100):
        minutes = math.ceil(minutes)
        overall = (minutes - 100)*2 + 150
        print('It costs', overall,' hrn')
        break
    else:
        print('ERROR. Number of minutes cant be negative. Try again')    
        continue
        
