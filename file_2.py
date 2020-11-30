from file_1 import one

class two(one):
    def second(self):
        self.var2=one.var#как вот здесь
        # получить var из другого файла
        print(self.var2)


run=two()
run.second()