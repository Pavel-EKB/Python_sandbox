import contextlib
@contextlib.contextmanager
def context():
    print (u'вход в блок')
    try:
        yield {}
    except RuntimeError as err:
        print ('error: ')
    finally:
        print (u'выход из блока')

print ('Проверим работоспособность кода:')
with context() as fp:
    print (u'блок')

print ('\nПопробуем возбудить исключение внутри блока.')
with context() as value:
    raise RuntimeError

print ('\nЕще пример')
@contextlib.contextmanager
def bold_text():
    print ('<b>')
    yield # код из блока with выполнится тут
    print ('</b>')

with bold_text():
    print ("Hello, World")
