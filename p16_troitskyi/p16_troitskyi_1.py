from functools import reduce
while True:
    try:
        num = int(input('Enter number of pages. '))
    except ValueError:
        print('Enter an integer.')
        continue
    if num % 16 != 0:
        print('Enter number that divisible by 16.')
        continue
    elif num not in range(16, 1281):
        print('Enter number that is in range from 16 to 1280')
    else:
        break
while True:
    t_f = input('True or False? ')
    if t_f.lower() == 'true' or t_f == '1':
        t_f = True
        break
    elif t_f.lower() == 'false' or t_f == '0':
        t_f = False
        break
    else:
        print("Enter 'True' or '1' if constant is true, enter 'False' or '0' if constant is false. ")
        continue
def decor(func, z = t_f):  
    def inner():
        lst = []
        if z == False:
            for a in func(num):
                lst.append(a)
            print(lst)
        else:
            for a in func(num):
                sheet = []
                for i in range(4, len(a)+1, 4):
                    sheet.append((a[i-4], a[i-3], a[i-2], a[i-1]))
                lst.append(sheet)
            print(lst)   
    return inner
@decor
def cpb(num):
    for page in range(16, num+1, 16):
        yield reduce(lambda q,w: q+w, [[page-ind, ind+1+page-16, ind+2+page-16, page-1-ind] for ind in range(0, 8, 2)])

print('Book: ')
cpb()
print('Number of sheets: ',int(num/16))
