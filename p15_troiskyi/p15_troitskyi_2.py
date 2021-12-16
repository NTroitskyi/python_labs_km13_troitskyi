Cards = ['A', *range(2, 11), 'J', 'Q', 'K']
M = ['diamonds', 'clubs', 'hearts', 'spades']
def gen(cards, m):
    for i in m:
        for a in cards:
            yield str(a) + ' ' + i
deck = gen(Cards, M)
while True:
    print(next(deck))
