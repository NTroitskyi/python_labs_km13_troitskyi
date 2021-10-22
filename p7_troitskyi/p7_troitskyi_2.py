while True:
    Rk = input('R: ')
    try:
        Rk = int(Rk)
    except ValueError:
        print('You must input integer from 0 to 255. Try again.')
        continue
    if Rk not in range(0, 266):
        print('You must input integer from 0 to 255. Try again.')
        continue
    else:
        print('Rk = ', Rk)
        break
    

while True:  
    Gk = input('G: ')
    try:
        Gk = int(Gk)
    except ValueError:
        print('You must input integer from 0 to 255. Try again.')
        continue
    if Gk not in range(0, 266):
        print('You must input integer from 0 to 255. Try again.')
        continue
    else:
        print('Gk = ', Gk)
        break
        
while True:
    Bk = input('B: ')
    try:
        Bk = int(Bk)
    except ValueError:
        print('You must input integer from 0 to 255. Try again.')
        continue
    if Bk not in range(0, 266):
        print('You must input integer from 0 to 255. Try again.')
        continue
    else:
        print('Rk = ', Bk)
        break


HEX = {'0' : '0',
       '1' : '1',
       '2' : '2',
       '3' : '3',
       '4' : '4',
       '5' : '5',
       '6' : '6',
       '7' : '7',
       '8' : '8',
       '9' : '9',
       '10' : 'A',
       '11' : 'B',
       '12' : 'C',
       '13' : 'D',
       '14' : 'E',
       '15' : 'F'}


Rc = str(Rk//16)
Ro = str(Rk % 16)
Gc = str(Gk//16)
Go = str(Gk % 16)
Bc = str(Bk//16)
Bo = str(Bk % 16)
print(Rk%16)
list_before = [Rc, Ro, Gc, Go, Bc, Bo]
print(list_before)
for a in list_before:
    print(HEX.get(a), end ='')