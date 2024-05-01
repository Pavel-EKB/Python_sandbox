print ('7.2.1 — Вложенный генератор внутри генератора — двумерная из двух одномерных')
#Общий синтаксис: [[expression for y in iter2] for x in iter1]
w, h = 5, 3  # зададим ширину и высотку матрицы
matrix = [[0 for x in range(w)] for y in range(h)]
print(matrix)

print ('\n7.3 — Генератор итерирующийся по генератору')
list_c = [x**2 for x in [x for x in range(-2, 4)]]
print(list_c)  # [4, 1, 0, 1, 4, 9]