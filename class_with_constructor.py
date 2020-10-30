class Something:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def describe(self):
        print("My name is {}, I am {} years and my size is {}".format(self.name, self.age, self.size))
        return ("My name is {}, I am {} years and my size is {}".format(self.name, self.age, self.size))



asds=Something(name="Max",age="25",size="full")
asds.describe()
