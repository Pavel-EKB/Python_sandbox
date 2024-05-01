doit = {'neg':lambda x: x-1, 'abs':lambda x: abs(x)-1, 'zero':lambda x: x}
a = [-3, 10, 0, 1]
for i in a:
    if i < 0:
        print(doit['abs'](i))
    elif i > 0:
        print(doit['neg'](i))
    else:
        print(doit['zero'](i))