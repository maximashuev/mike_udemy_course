from Venmo.sql_base import SQL_BASE
from Venmo.login_page import Login

class MainManu():
    def __init__(self,username):
        self.username=username

    def main_menu(self):
        print("===================================")
        print("             Main Menu")
        print("1.Current Balance")
        print("2.Send money")
        print("3.Request money")
        print("4.Withdraw money")
        print("5.Close account")
        print("6.Exit")
        print("===================================")
        action=input("Type menus number:")
        if action=="5":
            action = input("Please,enter username:")
            if action==self.username:
                SQL_BASE.close_account_by_name(SQL_BASE.get_connection(self),action)
            else:

                print("")
                print("Account username is incorrect.")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                MainManu.main_menu(self)
        elif action=="6":
            print("Have a good day.")
            quit()
        else:
            print("")
            print("This feature is under development.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            MainManu.main_menu(self)




