import queue

q = queue.Queue()
l = []

for i in range(5):
    l.append(i)
    q.put(i)

print ('Вносим потоки:')
print (*l)
print ('Извлекаем потоки:')
while not q.empty():
    print(q.get(), end=' ')