list = []
while True:
    element = input('Input list elements one by one. When you want to stop just press Enter button : ' ) #just for data inputing and list creating
    if element.lower() == '':
        break
    list.append(element)
    
newlist = [p + ',' for p in list]
leng = len(list)
if leng > 2:                #I didnt know how to delete commas for leng >= 2 so did this
    del newlist[-1]
    del newlist[-1]
    newlist.append(list[-2])
    newlist.append(list[-1])

if leng == 1:
    for c in range(leng):
        print(list[c], end=' ')
        break
while leng == 2:
    list.insert(-1, 'and')
    for c in range(leng + 1):
        print(list[c], end=' ')
    break
if leng > 2:
    newlist.insert(-1, 'and')
    for c in range(leng + 1):
        print(newlist[c], end=' ')    #Results