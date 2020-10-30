class MobilePhone:
    def info(self,_os, _os_vendor):
        print("Mobile device based on {} by {}".format(_os, _os_vendor))
        return ("Mobile device based on {} by {}".format(_os, _os_vendor))

    def call(self, phone_number, _os):
        if isinstance(phone_number, int) and len(str(phone_number)) == 11:
            print("Calling to {} from {} phone".format(phone_number, _os))
            return ("Calling to {} from {} phone".format(phone_number, _os))
        else:
            print("Wrong phone number")
            return ("Wrong phone number")

class iPhone(MobilePhone):
    pass

class AndroidPhone(MobilePhone):
    pass

apple_phone = iPhone()
apple_phone.call(12345678978, "iOS")
apple_phone.info("iOS", "Apple")
