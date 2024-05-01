class SimpleIterator:
   def __iter__(self):
       return self
   def __init__(self):
       self.tmp = -1
   def __next__(self):
       self.tmp += 1
       return self.tmp

si = SimpleIterator()
print(next(si))
print(next(si))
print(next(si))
del si