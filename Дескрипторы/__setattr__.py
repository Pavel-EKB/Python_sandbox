class NoSetters:
    attr = "class attribute"
    def __setattr__(self, name, val):
        print("not setting {0}={1}".format(name,val))

no_setters = NoSetters()
no_setters.a = 1            # not setting a=1
no_setters.attr = 1         # not setting attr=1
no_setters.__dict__         # {}
no_setters.attr             # "class attribute"
no_setters.a                # AttributeError