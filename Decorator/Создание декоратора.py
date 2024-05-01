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

first_test_wrapped = simple_decore(first_test)
second_test_wrapped = simple_decore(second_test)

first_test()
second_test()

first_test = first_test_wrapped
second_test = second_test_wrapped
first_test()
second_test()

#можно записать так
@simple_decore
def first_test():
    print("Test function 1")
