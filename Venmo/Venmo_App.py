from Venmo.login_page import Login
from Venmo.main_menu import MainManu

class Start :
    def start(self):
        user=Login()
        user.welcome_page()
        MainManu(user.username).main_menu()

if __name__=="__main__":
    Start().start()




