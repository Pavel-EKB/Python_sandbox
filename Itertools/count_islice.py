from itertools import islice
from itertools import count

for i in islice(count(10, 2), 5):
    print(i)
#count(start=0, step=1)
#islice - сколько выдать элементов