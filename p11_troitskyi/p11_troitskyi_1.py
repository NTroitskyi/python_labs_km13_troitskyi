tail = []
def cons(head, tail):
    list1 = []
    list1.append(head)
    list1 = list1 + list(tail)
    return list1
print(cons(1, tail))

l = cons(3,
        cons(2,
            cons(1, [])))
print(l)


print('All tests good!')


lst = [1, 2, 3]
def sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum(lst[1:])
print(sum(lst))

        
        
