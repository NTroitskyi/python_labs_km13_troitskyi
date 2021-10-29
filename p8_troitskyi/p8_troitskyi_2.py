import math         #sorry for long code
print('ax**2+bx+c=0')
while True:         #excluding the Value Error while entering variables(string 3 - 26)
    try:
        a = float(input('a = '))
    except ValueError as er:
        print(er)
        continue
    else:
        break
while True:
    try:
        b = float(input('b = '))
    except ValueError as er:
        print(er)
        continue
    else:
        break
while True:
    try:
        c = float(input('c = '))
    except ValueError as er:
        print(er)
        continue
    else:
        break
D = float(b**2 - 4*a*c) 
try:        #the most useless thing I ever done
    D = math.sqrt(D)
except ValueError as nope:
    print(nope)

try:        #raising Errors and calculating roots
    if D < 0:
        raise ValueError('No roots bro...')
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)
except ZeroDivisionError as dude:
    print(dude)
else:
    if x1 == x2:
        print('x = ', round(x1, 3))
    elif x1 != x2:
        print('x1 = ',round(x1),
        'x2 = ',round(x2))



  