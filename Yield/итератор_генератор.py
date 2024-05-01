# Создание арифметической прогрессии с помощью класса итератора:
print ('# Создание арифметической прогрессии с помощью класса итератора:')
class AP:
    def __init__(self, a1, d, size):
        self.ele = a1
        self.diff = d
        self.len = size
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.len:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return self.ele
        else:
            self.count += 1
            self.ele += self.diff
            return self.ele

for ele in AP(1, 2, 10):
    print(ele)

#Генерация арифметической прогрессии с помощью функции генератора:
print('\n#Генерация арифметической прогрессии с помощью функции генератора:')

def AP(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1

for ele in AP(1, 2, 10):
    print(ele)