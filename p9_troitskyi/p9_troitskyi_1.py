import numpy as np
import itertools
while True:
    def random_matrix(dim):
        Matrix = np.random.randint(10, size = (dim, dim))
        return Matrix

    while True:     
        try:
            dim = int(input("Enter a dimension. Don't even try numbers more that 9: "))
            M = random_matrix(dim)
        except Exception as er:
            print(er)
            continue
        else:
            if dim > 9:
                print("I said don't try numbers more that 9. Learn it and try again.")
                continue
            else:
                break
    
    print(M)
    list1 = []
    for a in range(dim):
        list1.append(str(a))
    b = str(''.join(list1))

    def perm(x):  #function of permutation aas you can see
        p = list(itertools.permutations(str(b), x))
        return p

    pe = perm(dim) #as function

    def prod(mutations, matrix):  #function of product
        list2 = []
        for k in mutations:
            prod = 1
            index = 0
            for l in range(len(k)):
                joiner = matrix[index][int(k[l])]
                prod *= joiner
                index += 1
            list2.append(prod)
        return(list2)

    def inversion(inv):     #I had to make this function to done function of sum correctly
        list3 = []
        for p in range(len(inv)):
            inve = inv[p]
            inv_number = 0
            for q in range(len(inve)):
                for w in range(q + 1, len(inve)):
                    if inve[q]>inve[w]:
                       inv_number += 1
            list3.append(inv_number)
        return list3

    def sum(inv, pro):    #function of sum
        sum = 0
        for e in range(len(inv)):
            if int(inv[e]) % 2 == 0:
                dodanok = int(pro[e])
            if int(inv[e]) % 2 != 0:
                dodanok = int(pro[e])*(-1)
            sum += dodanok
        return sum        
 

    el = inversion(pe)
    primo = prod(pe, M)

    print('det = ',sum(el, primo))
    choise = input('Enter T if you want to repeat: ')
    if choise.lower() == 't':
        continue
    else:
        break

import sys
sys.exit()