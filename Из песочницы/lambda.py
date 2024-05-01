tmp = {}
for i in range(10):
    tmp[i] = lambda: i

print (tmp[0]())
print (tmp[1]())
print (list(tmp))

tmp = {}
for i in range(10):
    tmp[i] = lambda i = i: i
print (tmp[0]())
print (tmp[1]())