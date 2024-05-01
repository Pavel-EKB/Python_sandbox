class GentleGuy:
    def __getattribute__(self, name):
        if name.endswith("_please"):
            return object.__getattribute__(self, name.replace("_please", ""))
        #raise AttributeError("And the magic word!?")

gentle = GentleGuy()
gentle.coffee = "some coffee"
#gentle.coffee           # AttributeError
print (gentle.coffee_please)    # "some coffee"