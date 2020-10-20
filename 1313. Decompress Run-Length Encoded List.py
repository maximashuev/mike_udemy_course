"""
В этом задании нужно реализовать функцию unzip_list(zipped_list: list)
которая будет распаковывать список элементов по следующему алгоритму и возвращать результат в качестве списка элементов.
В запакованном списке хранятся элементы следующего вида "3|4" где первое число это количество повторений, а второе
это число которое нужно повторить. Таким образом элемент вида"3|4" будет распакован в последовательность чисел 4, 4, 4.
Все эти последовательности нужно распаковать в один список.
Если какой-то из элементов не содержит | но приводится к числу, то просто добавлять его числовое представление.
"""

def unzip_list(zipped_list: list):
    print("Input",zipped_list)
    new_list = []
    for part in zipped_list:
        # print(len(part))
        if "|" in part:
            mylist=part.split("|")
            # print("upper mylist",mylist)
            for subitem in mylist:
                new_list.append(int(subitem))

        elif len(part)<2:
            for subitem in part:
                if len(subitem) < 2:
                    for item in subitem:
                        new_list.append(1)
                        new_list.append(int(item))
                else:
                    for item in subitem:
                        new_list.append(int(item))

        else:
            for side in part:
                new_list.append(int(side))
    print("new_list", new_list)
    deziped=[]
    i=0
    while i <len(new_list):

        for d in range(new_list[i]):
            deziped.append(new_list[i + 1])
        i=i+2
    print("deziped",deziped,"\n")
    return deziped
    pass
unzip_list(["1|2","3|4"])
unzip_list(["1|4", "3|8", "6|1"])
unzip_list([["4"],["2","5"],["1"]])
unzip_list(["4","2|5","1"])
unzip_list( ["15|1"])






# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.

# def decompressRLElist(nums: list):
#     decompressed = []
#
#     for i in range(0, len(nums) - 1, 2):
#         decompressed = decompressed + nums[i] * [nums[i + 1]]
#     print(decompressed)

#     return decompressed
#
#
# decompressRLElist([1, 2, 3, 4])
