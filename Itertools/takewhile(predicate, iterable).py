from itertools import takewhile

data = list(takewhile(lambda x: x<5, [1,4,6,4,1]))
print(data) # [1, 4]
