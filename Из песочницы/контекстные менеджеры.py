with open("./file.txt", "w") as fp:
    fp.write("Hello, World")

class Hello:
    def __del__(self):
        print (u'destructor')

f = Hello()
c = Hello()
e = Hello()
del e
del c
c=f
e=f
del f

class Hello:
    def __del__(self):
        print (u'деструктор')
    def __enter__(self):
        print (u'вход в блок')
    def __exit__(self, exp_type, exp_value, traceback):
        print (u'выход из блока')

f = Hello()
c = f
e = f
d = f
del d
del e
del c
del f

with Hello():
    print (u'мой код')