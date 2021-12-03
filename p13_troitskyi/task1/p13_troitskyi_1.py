import string
gadsby = "gadsby.txt"

def load_text():
    inFile = open(gadsby, 'r')    
    text = inFile.read()
    text = text.lower()
    text = text.split()
    text = ''.join(text)
    for a in text:
        if a in string.punctuation:
            text = text.replace(a, '')
    return text

letters = 'qwertyuiopasdfghjklzxcvbnm'


def percentage(text, letters):
    percents = []
    for letter in letters:
        number = text.count(letter)
        percents.append([letter,':', str(round((number*100/len(text)),3)), '%'])
    p = sorted(percents, key = lambda q: float(q[2]), reverse = True)
    return p



for i in percentage(load_text(), letters)[:5]:
    print(''.join(i))
print('...')
for i in percentage(load_text(), letters)[-5:]:
    print(''.join(i))