set_a = {1, 2, 3}
set_b = {2, 1}                  # порядок элементов не важен!
set_c = {4}
set_d = {1, 2, 3}

print(set_a.isdisjoint(set_c))  # True - нет общих элементов
print(set_b.issubset(set_a))    # True  - set_b целиком входит в set_a, значит set_b - подмножество
print(set_a.issuperset(set_b))  # True - set_b целиком входит в set_a, значит set_a - надмножество

#При равенстве множеств они одновременно и подмножество и надмножество друг для друга
print(set_a.issuperset(set_d))  # True
print(set_a.issubset(set_d))    # True
