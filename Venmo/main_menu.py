from Venmo.sql_base import close_account_by_name,get_connection
import Venmo.login_page


def main_menu():
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
        # try:
        #     print(action,login_username.get_username)
        #     assert action==login_username.get_username
        #     close_account_by_name(get_connection(),action)
        # except:
        #     print("Not existing account")
        #     close_account_by_name(get_connection(), action)



    elif action=="6":
        print("Have a good day.")
        quit()

