def tran_to_string(some_list):
    result = ""
    for element in some_list:
        result += str(element)
    return result


print(tran_to_string([1,"hello",True]))

a = 10
if a == True:
    print("Всё верно")
elif a:
    print("Всё почти верно")
else:
    print("Всё не так как кажется")

a = None
if a or None:
    print("Всё верно")

a = True or True and  False
print(a)

s = "Привет, %s {}!".format("Николай")
print(s)