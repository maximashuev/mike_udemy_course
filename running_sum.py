"""
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""


def running_sum(some_list: list):
    if isinstance(some_list,list):
        print("It is a list",some_list)

        if len(some_list)<= 1:
            print("Empty list")
            return some_list

        elif not all(isinstance(z,(int,float))for z in some_list):
            print(some_list,"Плохой список")
            return ("Плохой список")
        else:
            tmp=0
            new_list=[]
            for i in some_list:
                tmp++i # == to tmp=tmp+i
                new_list.append(tmp)
            print(new_list)
            return new_list


    else:
        print("Это не список")
        return ("Это не список")
    pass

running_sum([1,2,3,4])
# running_sum([3,"1",2,10,1])
# running_sum([])
# running_sum([1])
# running_sum(None)