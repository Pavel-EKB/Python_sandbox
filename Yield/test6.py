#код запустит бесконечный цикл, для остановки которого нужно нажать Ctrl + break.
def find_prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

for ele in find_prime():
    print(ele)