
alist = ['Python', 'Java', 'C', 'C++', 'CSharp']

def list_items():
    for item in alist:
        yield item

gen = list_items()

iter = 0

while iter < len(alist):
    print(next(gen))
    iter += 1