# Свою реализацию пишите внутри функции, не меняя её имя.
# Функция должна быть использована в качестве декоратора для других функций.


#solution 1
def my_decorator(func):
    def wrap(*args):
        print(*args)
        if isinstance(*args,(int,str,list,dict,bool,tuple,set)):
            print("Функция вернула значение типа {}:{}".format(type(*args),func(*args)))
            return "Функция вернула значение типа {}:{}".format(type(*args), func(*args))
        else:
            print("Функция ничего не вернула")
            return "Функция ничего не вернула"

    return wrap

#solution 2
# def my_decorator(f):
#     def wrapper(*args):
#         if f(*args) is None:
#             return "Функция ничего не вернула"
#         return "Функция вернула значение типа {}: {}".format(str(type(f(*args))), f(*args))
#     return wrapper


@my_decorator
def test(h):
    return h

test(123)
test("dsf")
test({})
test([])
test(True)
test(())
test(None)


