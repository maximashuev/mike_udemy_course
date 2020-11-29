from Venmo.login_page import Login
from Venmo.main_menu import MainManu

class Start (Login,MainManu):
    def start():
        Login.welcome_page()
        MainManu.main_menu()

# if __name__=="__main__":
#     Login.welcome_page()
#     MainManu.main_menu()


start = Start()
start.welcome_page()
start.main_menu()