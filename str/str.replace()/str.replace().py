x = 'все вхождения подстроки `old` заменены на подстроку `new`'
print (x.replace('`', '-'))
# 'все вхождения подстроки -old- заменены на подстроку -new-'

x = '2 вхождения подстроки `old` заменены на подстроку `new`'
print (x.replace('`', '~', 2))
# '2 вхождения подстроки ~old~ заменены на подстроку `new`'

print (x.replace('old', 'старая').replace('new', 'новая'))
# 'все вхождения подстроки `старая` заменены на подстроку `новая`'

x = 'Привет_буфет!'
print (x.replace('_буфет', ''))