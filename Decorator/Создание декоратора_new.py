def first_test():
    print("Test function 1")
def second_test():
    print("Test function 2")

def simple_decore(fn):
    def wrapper():
        print("Run function")
        fn()
        print("Stop function")
    return wrapper

@simple_decore
def first_test():
    print("Test function 1_")

@simple_decore
def second_test():
    print("Test function 2_")

first_test()
second_test()