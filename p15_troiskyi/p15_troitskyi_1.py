from math import factorial
def inputing():
    try:
        pow = int(input('Enter a power: '))
    except Exception:
        return False
    if pow < 0:
        return False
    else:
        return pow
    
while True:
    a = inputing()
    if a == False:
        if a == 0:
            print(1)
            break
        else:
            print('Wrong data')
            continue
    else:
        def pascale(power):
            coef = lambda power, k: round(factorial(power)/(factorial(k)*factorial(power-k)))
            for pow in range(power+1):
                yield ' '.join(str(coef(pow, s)) for s in range(pow+1))
               
        newton = pascale(a)
        for e in newton:
            print(e)
        break

