class StuffHolder:
    stuff = "class stuff"

a = StuffHolder()
b = StuffHolder()
a.stuff     # "class stuff"
b.stuff     # "class stuff"

b.b_stuff = "b stuff"
b.b_stuff   # "b stuff"
#a.b_stuff   # AttributeError

StuffHolder.__dict__    # {... 'stuff': 'class stuff' ...}
a.__dict__              # {}
b.__dict__              # {'b_stuff': 'b stuff'}

a.__class__             # <class '__main__.StuffHolder'>
b.__class__             # <class '__main__.StuffHolder'>

#Присвоим новый атрибут
#a.new_stuff                 # AttributeError
#b.new_stuff                 # AttributeError

StuffHolder.new_stuff = "new"
StuffHolder.__dict__        # {... 'stuff': 'class stuff', 'new_stuff': 'new'...}
a.new_stuff                 # "new"
b.new_stuff                 # "new"