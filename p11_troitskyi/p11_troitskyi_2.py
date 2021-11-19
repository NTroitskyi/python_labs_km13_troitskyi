def rrange(begin, end, step = 1):
    list1 = []
    if step > 0:
        if begin < end:
            list1.append(begin)
            list1.extend(rrange(begin + step, end, step))
        else:                 #cosmetic...
            pass
    elif step < 0:
        if begin > end:
            list1.append(begin)
            list1.extend(rrange(begin + step, end, step))
        else:
            pass
    return list1


x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)