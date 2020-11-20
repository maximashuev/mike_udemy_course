class HowMuch:
    deleted_amount=0
    created_amount=0
    exist_amount=0

    def __init__(self):
        self.up()
        # self.__del__()
        self.exist()

    @classmethod
    def up(cls):
        cls.created_amount += 1

    @classmethod
    def __del__(self):
        self.deleted_amount+=1

    @classmethod
    def exist(cls):
        cls.exist_amount=cls.created_amount-cls.deleted_amount






    def describe(self):
        print("HowMuch instances: deleted - {}, created - {}, exist - {}".format(self.deleted_amount,self.created_amount,self.exist_amount))
        return ("HowMuch instances: deleted - {}, created - {}, exist - {}".format(self.deleted_amount,self.created_amount,self.exist_amount))

