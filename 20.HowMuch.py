class HowMuch:
    amount=0
    def __init__(self):
        self.up()

    @classmethod
    def up(cls):
        cls.amount += 1

    @classmethod
    def count(self):
        return ("{} instances of HowMuch class were created".format(self.amount))

