TRUE = lambda x: lambda y: x
TRUE.__name__ = "TRUE"
FALSE = lambda x: lambda y: y
FALSE.__name__ = "FALSE"
AND = lambda p: lambda q: p(q)(p)

print (AND(TRUE)(TRUE).__name__)
print (AND(TRUE)(FALSE).__name__)
