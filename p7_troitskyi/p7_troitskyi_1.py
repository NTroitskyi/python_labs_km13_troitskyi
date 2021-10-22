format_tuple = ('Liverpool', 845.15, 21, 134, 358.45, 'price')
strin = 'The initial lot {5} of ${4} at the {0} auction exceeded the expected {5} by {2}%, but the lot with number {3} was nevertheless sold for ${1}'
print(strin.format('Liverpool', round(845.15), 21, str.zfill(str(134), 4), round(358.45, 1), 'price')) 