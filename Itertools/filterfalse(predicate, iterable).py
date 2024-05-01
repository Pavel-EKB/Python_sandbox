from itertools import filterfalse

def greater_than_five(x):
    return x > 5

data = list(
    filterfalse(
        greater_than_five,
        [6, 7, 8, 9, 1, 2, 3, 10]
    )
)

print(data) # [1, 2, 3]