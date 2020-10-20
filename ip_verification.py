def is_ip(string:str):
    print(string)
    pieces = string.split('.')
    # print(pieces)
    for x in pieces:
        if not x.isdigit():
            print("false-not digit")
            return False

        if len(pieces) != 4:
            print("false-not IP len")
            return False
        i=int(x)
        if (i<0 or i>255):
            print("not 0-255")
            return False
    print("true")
    return True

is_ip("192.168.1.a")
is_ip("192.168.1.17")
is_ip("192.125")
is_ip("1921.168.1.256")

