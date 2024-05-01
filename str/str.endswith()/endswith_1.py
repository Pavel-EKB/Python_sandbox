#str.endswith(suffix[, start[, end]])
x = 'заканчивается указанным суффиксом suffix'
print (x.endswith('suffix'))
# True
print (x.endswith('иксом'))
# False
print (x.endswith('иксом',0 ,-7))
# True