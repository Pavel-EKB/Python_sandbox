from itertools import compress

letters = 'ABCDEFG'
bools = [True, False, True, True, False]

data = list(compress(letters, bools))
print(data) # ['A', 'C', 'D']