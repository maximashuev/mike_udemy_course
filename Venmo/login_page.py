from Venmo.sql_base import SQL_BASE


class Login(SQL_BASE):
    def welcome_page(self):
        print("===================================")
        print("         Welcome to Venmo")
        action = input("Are you existing customer?(Y/N):")
        if action == "y":
            Login.login_username(self)
        else:
            print("===================================")
            print("         To create account")

            Login.create_account(self)

    def create_account(self):
        con = SQL_BASE.get_connection(self)
        self.username = input("Create username:")
        try:
            assert self.username == SQL_BASE.verify_username(self.get_connection(), self.username)
            print("Customer with given username already exist.\nPlease enter different username.")
            Login.create_account(self)
        except:
            pass
        self.password = input("Create password:")
        print("===================================")
        SQL_BASE.insert_data(con, self.username, self.password)


    def login_username(self):
        self.get_username = input("Enter Username:")
        try:
            assert self.get_username == SQL_BASE.verify_username(self.get_connection(), self.get_username)
            Login.login_password(self)


        except:
            pass
            print("Customer with such username is not exist.")
            Login.login_username(self)
        return self.get_username

    def login_password(self):
        get_password = input("Enter Password:")
        try:
            assert get_password == SQL_BASE.verify_password(self.get_connection(), self.get_username)
            print("Logged In successfully.Hello,{}.".format(self.get_username))
        except:
            print("Password is incorrect")
            Login.login_password(self)
