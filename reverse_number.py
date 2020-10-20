def reverse_number(number):
    print(type(number))
    print(number)
    if isinstance(number,int):
        if number > 0:
            strr = str(number)
            x = int(strr[::-1])
            print(x,"\n")
            return x
        # reverse with -
        elif int(number) < 0:
            number = number * -1
            number = (int((str(number)[::-1]))) * -1
            print(number,"\n")
            return number
        # reverse float
        else:
            # fl=str(number).split(".")
            # print(fl)
            print("d","\n")

    elif isinstance(number,float):
        if number >0:
            reversed_float=[]
            fl=str(number).split(".")

            for re in fl:
                re=re[::-1]
                reversed_float.append(re)
            print(float('.'.join(reversed_float)),"\n")
            return (float('.'.join(reversed_float)))
        else:
            number=number*-1
            rev_list=[]
            sep=str(number).split(".")
            for asd in sep:
                rev_list.append(asd[::-1])
            print((float(".".join(rev_list)))*-1,"\n")
            return ((float(".".join(rev_list)))*-1)

    else:
        isinstance(number,str)
        print("Number is a string","\n")
        return number



reverse_number(123)
reverse_number(-4568)
reverse_number(123.001)
reverse_number("asdfZLFJB")
reverse_number(-15962699.99101038)

# def reverse(x):
#     y = ""
#     if int(x) <= -1:y="-";x = int(x)*-1
#     output =  int(y+str(x)[::-1])
#     if output >= -2**31 and output <= 2**31 - 1:return output
#     else: return 0
#
# print(reverse(-123))
