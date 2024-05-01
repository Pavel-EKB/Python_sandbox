def hello(self):
    print ('Hello!')

NewClass = type('NewClass', (), {'hello': hello, 'val': 3})
a = NewClass()
a.hello()
print (a.val)

a.score = 4
print (NewClass.__dict__)
print (a.__dict__)