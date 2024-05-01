class Optimist:
    attr = "class attribute"

    def __getattribute__(self, name):
        return("{0} is great!".format(name))

    def __len__(self):
        print("__len__ is special")
        return 0

o = Optimist()
o.instance_attr = "instance"

print (o.attr)          # attr is great!
print (o.dark_beer)     # dark_beer is great!
print (o.instance_attr) # instance_attr is great!
print (o.__len__)       # __len__ is great!
print (len(o))          # __len__ is special\n 0