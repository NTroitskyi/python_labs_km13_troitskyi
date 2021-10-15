a = input('phrase 1: ')
b = input('phrase 2: ')

set1 = set(a)
set2 = set(b)

set1.discard(' ') #deleting space from set
set2.discard(' ')

print(set1)
print(set2)

if set1.intersection(set2) == set2:
        print('U can')
else:
        print("U can't")