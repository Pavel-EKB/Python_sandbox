from itertools import dropwhile

data = list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
print(data) # [6, 4, 1]

from itertools import dropwhile

def greater_than_five(x):
    return x > 5

data = list(
    dropwhile(
        greater_than_five,
        [6, 7, 8, 9, 1, 2, 3, 10]
    )
)

print(data) # [1, 2, 3, 10]