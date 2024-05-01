class SmartyPants:
    def __getattr__(self, attr):
        return ("Yep, I know" + str(attr))
    tellme = "It's a secret"

smarty = SmartyPants()
smarty.name = "Smartinius Smart"

print (smarty.quicksort)   # Yep, I know quicksort
print (smarty.python)      # Yep, I know python
print (smarty.tellme)      # "It's a secret"
print (smarty.name)        # "Smartinius Smart"
