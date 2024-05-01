alist = ['Python', 'Java', 'C', 'C++', 'CSharp']

def list_items():
    for item in alist:
        yield item

gen = list_items()

for item in gen:
    print(item)