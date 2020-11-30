from Venmo.sql_base import SQL_BASE

class Login():
    def __init__(self):
        self.username= "+++++"
        self.password="-----"

    def welcome_page(self):
        print("===================================")
        print("         Welcome to Venmo")
        action = input("Are you existing customer?(Y/N):")
        if action == "y":
            self.login_username()
        else:
            print("===================================")
            print("         To create account")
            self.create_account()

    def create_account(self):
        con = SQL_BASE.get_connection(self)
        self.username = input("Create username:")
        try:
            assert self.username == SQL_BASE.verify_username(SQL_BASE.get_connection(self), self.username)
            print("Customer with given username already exist.\nPlease enter different username.")
            self.create_account()
        except:
            pass
        self.password = input("Create password:")
        print("===================================")
        SQL_BASE.insert_data(con, self.username, self.password)

    def login_username(self):
        self.username = input("Enter Username:")
        try:
            assert self.username == SQL_BASE.verify_username(SQL_BASE.get_connection(self), self.username)
            self.login_password()
        except:
            print("Customer with such username is not exist.")
            self.login_username()

    def login_password(self):
        self.password = input("Enter Password:")
        try:
            assert self.password == SQL_BASE.verify_password(SQL_BASE.get_connection(self), self.username)
            print("Logged In successfully.Hello,{}.".format(self.username))
        except:
            print("Password is incorrect")
            self.login_password()
