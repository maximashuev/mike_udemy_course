"""
write a function that takes an array of integers  and returns the sum of all elements

"""


def sumArray(sum_array: list) -> 15:
    # 1 line solusion
    print((sum(sum_array)), "        1 line solusion")
    # for loop solution
    sum1 = 0
    for item in sum_array:
        sum1 = sum1 + item  # same as sum1+=item

    print(sum1, "        'for' loop solution")


sumArray([1, 2, 3, 4, 5])
