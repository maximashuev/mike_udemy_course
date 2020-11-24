from Venmo.sql_base import get_connection,insert_data,verify_username,verify_password


def welcome_page():
    print("===================================")
    print("         Welcome to Venmo")
    action = input("Are you existing customer?(Y/N):")
    if action == "y":
        login_username()
    else:
        con=get_connection()
        try:
            print("===================================")
            print("         To create account")
            username=input("Enter username:")
            password=input("Enter password:")
            print("===================================")
        except:
            print("Неверно введены данные")
        else:
            insert_data(con,username,password)


def login_username():
    global get_username
    get_username = input("Enter Username:")
    try:
        assert get_username==verify_username(get_connection(),get_username)
        login_password()

    except:
        print("Not valid username")
        login_username()
    return get_username

def login_password():
    get_password=input("Enter Password:")
    try:
        assert get_password==verify_password(get_connection(),get_username)
        print("Login successfully.Hello,{}.".format(get_username))
    except:
        print("Password is incorect")
        login_password()