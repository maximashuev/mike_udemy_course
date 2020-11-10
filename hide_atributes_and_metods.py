class Solution:
    __property = None

    def get_property(self):
        return self.__property

    def set_property(self, input):
        print(input)
        if isinstance(input, int) and input > 0:
            print("Значение установлено")
            self.__property = input
            print(self.__property)

            return ("Значение установлено")
        else:
            print("Неверное значение")
            return ("Неверное значение")

