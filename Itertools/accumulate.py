#accumulate(iterable, func=operator.add, *, initial=None)
from itertools import accumulate

result = list(accumulate(range(10)))
print(result)

from itertools import accumulate
import operator

result = list(accumulate(range(1, 5), operator.mul))
print(result) # [1, 2, 6, 24] <- (1×1=1, 1×2=2, 2×3=6, и т.д.)

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print (list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))

# Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
from itertools import repeat
logistic_map = lambda x, _:  r * x * (1 - x)
r = 3.8
x0 = 0.4
inputs = repeat(x0, 36)     # only the initial value is used
print ([format(x, '3.2f') for x in accumulate(inputs, logistic_map)])