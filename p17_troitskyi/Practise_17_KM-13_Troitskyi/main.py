from factorial.factorial import fact
from exp_root.exp import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def fact_num():
    while True:
        try:
            num = int(input('Enter a natural number: '))
        except Exception:
            print('\nWrong value. Try again.')
            continue
        if num < 1:
            print('\nWrong value. Try again.')
            continue
        else:
            return num


def exp_num():
    while True:
        try:
            num = float(input('Enter a parameter: '))
        except Exception:
            print('\nWrong value. Try again.')
            continue
        else:
            return num

def root_log_num():
    while True:
        try:
            num = float(input('Enter a parameter(positive number): '))
        except Exception:
            print('\nWrong value. Try again.')
            continue
        if num < 0:
            print('\nWrong value. Try again.')
            continue
        else:
            return num

def log_base():
    while True:
        try:
            num = float(input('Enter a base(positive number that is not "1") : '))
        except Exception:
            print('\nWrong value. Try again.')
            continue
        if num < 0 or num == 1:
            print('\nWrong value. Try again.')
            continue
        else:
            return num

def main():
    while True:
        choice = input('\nEnter "1" if you want to find a factorial \nEnter "2" if you want to exponentiate a number \nEnter "3" if you want to find a root of number \nEnter "4" if you want to find logarithm \nEnter: ')
        if choice == '1':
            a = fact_num()
            print('\nFactorial of {0} is'.format(a),fact(a))
            break
        elif choice == '2':
            while True:
                choose = input('\nEnter "1" if you want to find a square \nEnter "2" if you want to find a cube \nEnter: ') 
                if choose == '1':
                    a = exp_num()
                    print('\nSquare of {0} is'.format(a), exp2(a))
                    break
                elif choose == '2':
                    a = exp_num()
                    print('\nCube of {0} is'.format(a), exp3(a))
                    break
                else:
                    print('\nWrong value. Try again.')
                    continue
            break
        elif choice == '3': 
            while True:
                choose = input('\nEnter "1" if you want to find a square root \nEnter "2" if you want to find a cubic root \nEnter: ')
                if choose == '1':
                    a = root_log_num()
                    print('\nSquare root of {0} is'.format(a), root2(a))
                    break
                elif choose == '2':
                    a = root_log_num()
                    print('\nCubic root of {0} is'.format(a), root3(a))
                    break
                else:
                    print('\nWrong value. Try again.')
                    continue
            break
        elif choice == '4':
            while True:
                choose = input('\nEnter "1" if you want to find a logarithm \nEnter "2" if you want to find a natural logarithm \nEnter "3" if you want to find a decimal logarithm \nEnter: ')
                if choose == '1':
                    a = root_log_num()
                    b = log_base()
                    print('\nLogarithm of {0} with base {1} is'.format(a, b), log(a, b))
                    break
                elif choose == '2':
                    a = root_log_num()
                    print('\nNatural logarithm of {0}'.format(a), ln(a))
                    break
                elif choose == '3':
                    a = root_log_num()
                    print('\nDecimal logarithm of {0}'.format(a), lg(a))
                    break
                else:
                    print('Wrong value. Try again.')
                    continue
            break
        else:
            print('Wrong value. Try again.')
            continue




if __name__ == '__main__':
        main()