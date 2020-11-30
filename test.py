def get_free_urinals(urinals):
    return print(urinals.replace("10", "1").replace("01", "1").replace("00","0"))


get_free_urinals("10001")
get_free_urinals("01010")
get_free_urinals("0")
get_free_urinals("1001000001")
    # if "11" in urinals:
    #     print("-1")
    #
    # count=0
    # stock=[]
    # for i in urinals:
    #     if len(stock)==0:
    #         stock.append(i)
    #     else:
    #         var=stock.pop()
    #         if var=="1":
    #             if i=="1":
    #                 print("-1")
    #                 return -1
    #             else:continue
    #         else:
    #             if i=="0":
    #                 count+=1
    # if len(stock) > 0:
    #     var = stock.pop()
    #     if var == "0":
    #         count+=1
    # print(count)
    # return count

