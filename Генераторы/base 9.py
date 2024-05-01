print ('9.1 Последовательный проход по нескольким спискам')
import itertools
l1 = [1, 2, 3]
l2 = [10, 20, 30]
result = [x*2 for x in itertools.chain(l1, l2)]
print (result)

print ('\n9.2 Транспозиция матрицы')
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print ('\nили\n')
transposed = list(map(list, zip(*matrix)))
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print ('\nzip*')
print (list(zip(*matrix)))
print ('zip')
print (list(zip(matrix)))