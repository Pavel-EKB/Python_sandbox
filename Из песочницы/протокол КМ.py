class Open(object):
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        try:
            self.fp = open(self.file, self.flag)
        except IOError:
            self.fp = open(self.file, "w")
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr):
        """ подавляем все исключения IOError """
        if exp_type is IOError:
            self.fp.close() # закрываем файл
            return True
        self.fp.close() # закрываем файл

with Open("asd.txt", "w") as fp:
    fp.write("Hello, World\n")