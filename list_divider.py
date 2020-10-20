

def split_list(some_list:list,divider):
    left=[]
    right=[]

    # if some_list is not type(list):
    #
    #     return print("This is not a list")
    for i in some_list:
        if divider not in some_list:

            return some_list
        elif i<divider:
            left.append(i)
        elif i == divider:
            continue
        else:
            right.append(i)
    print(left, right)
    return left,right

split_list([1,2,3,4,5,6,7],4)
split_list([1,2,3,4,5,6,7],8)
# split_list(1234567,8)
