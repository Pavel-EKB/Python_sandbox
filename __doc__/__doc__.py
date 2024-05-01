import os


class A:  # Для Python 2 — A(object)
    """Описание класса."""

    def func():
        """Описание функции."""


        # Для класса.
        A.__doc__  # 'Описание класса.'


        # Для объекта.
        a = A()
        a.__doc__  # 'Описание класса.'

        # Для функции.
        func.__doc__  # 'Описание функции.'


        # Для модуля.
        os.__doc__  # OS routines for NT or Posix depending on what system ...

print(A.__doc__)
a = A()
print (a.__doc__)
print (a.func.__doc__)
print (os.__doc__)