
Male = {}
Female = {}
count = 1880
while count<2020:                             #it took about 5 minutes on my computer to see the result, and I dont know how to fix it 
    names = "yob{}.txt".format(count)
    inFile = open(names, 'r')    
    text = inFile.read()
    text = text.split()
    extra_list_male = []
    extra_list_female = []
    for i in text:
        i_list = i.split(',')
        index = text.index(i)
        del text[index]
        text.insert(index, i_list)
    for i in text:
        if 'M' in i:
            extra_list_male.append(i)
        else:
            extra_list_female.append(i)


    l = sorted(extra_list_male, key = lambda q: int(q[2]), reverse=True)
    if l[0][0] not in Male:
        Male[l[0][0]] = 1
    else:
        Male[l[0][0]] += 1
    l1 = sorted(extra_list_female, key = lambda q: int(q[2]), reverse=True)
    if l1[0][0] not in Female:
        Female[l1[0][0]] = 1
    else:
        Female[l1[0][0]] += 1
    
    count += 1

Male = sorted(Male.items(), key = lambda q: -q[1])
Female = sorted(Female.items(), key = lambda q: -q[1])

for i in Male:
    print(i[0],':', i[1])
print('...')
for i in Female:
    print(i[0],':', i[1])
print('...')