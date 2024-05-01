f = [[]] * 3
f[0].append('a')
f[1].append('b')
f[2].append('c')

print (f)

c = [[], [], []]
print (hex(id(c[0])), hex(id(c[1])), hex(id(c[2])))
#('0x104ede7e8', '0x104ede7a0', '0x104ede908')


print (hex(id(f[0])), hex(id(f[1])), hex(id(f[2])))
#('0x104ede710', '0x104ede710', '0x104ede710')