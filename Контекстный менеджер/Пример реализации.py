class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        print (1)
        self.__name = name
    def get_name(self):
        print (5)
        return self.__name
    def post_work(self):
        print('Resource: close')

class ResourceForWith:
    def __init__(self, name):
        print (0)
        self.__resource = Resource(name)
        print (2)
    def __enter__(self):
        print (3)
        return self.__resource
    def __exit__(self, type, value, traceback):
        self.__resource.post_work()
        print (6)

with ResourceForWith('Worker') as r:
    print (4)
    print(r.get_name())
    print ('Все выполнили, вызываем __exit__')