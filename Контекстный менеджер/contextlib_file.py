from contextlib import contextmanager
@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()
with open_file('test.txt', 'w') as fw:
    fw.write('hello')