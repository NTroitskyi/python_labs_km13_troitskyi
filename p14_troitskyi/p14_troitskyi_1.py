import csv
Filename = 'Pentakill.csv'
with open(Filename, 'w') as Pentakill:
    columns = ['Song', 'Year']
    P = csv.DictWriter(Pentakill, fieldnames = columns)
    P.writeheader()
    P.writerow({'Song': 'Lightbringer', 'Year':'2014'})
    P.writerow({'Song': 'Edge of Night', 'Year':'2021'})
    P.writerow({'Song': 'Lost Chapter', 'Year':'2021'})
    P.writerow({'Song': 'Mortal Reminder', 'Year':'2017'})
    P.writerow({'Song': 'Tear of the Goddess', 'Year':'2017'})
    P.writerow({'Song': 'Last Stand', 'Year':'2014'})
    P.writerow({'Song': 'Deathfire Grast', 'Year':'2014'})

with open(Filename, 'r') as Pentakill:
    p = csv.DictReader(Pentakill)
    print(Pentakill.name)
    print(' - '.join(p.fieldnames))
    for a in p:
        print(a['Song'],'-', a['Year'])