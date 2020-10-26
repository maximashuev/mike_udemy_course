def zip_list(some_list:list):
    cur=some_list[0]
    count=1
    res=""
    for i in range(1,len(some_list)):
        el=some_list[i]
        if el==cur:
            count+=1
        else:
            if count==1:
                res+=str(cur)
            else:
                res+=str(count)+"|"+str(cur)

            res+=":"
            count=1
            cur=el


    if count>1:
        res += str(count) + "|" + str(cur)
    else:
        res += str(cur)
    # print(res)
    return res

zip_list([5,2,2,2,45,3,3,3,3,566])

































# def zip_list(some_list: list):
#     dic={}
#     for i in some_list:
#         if i in dic:
#             dic[i]=dic[i]+1
#         else:
#             dic[i]=1
#
#     print(dic)
#     listic=[]
#     for kay,val in dic.items():
#         if val==1:
#             listic.append(str(kay))
#         else:
#             listic.append(str(val)+"|"+str(kay))
#     print(":".join(listic))
#     return (":".join(listic))


# def zip_list(some_list: list):
#     cur = some_list[0]
#     count = 1
#     res = ""
#
#     for i in range(1, len(some_list)):
#         el = some_list[i]
#
#         if el == cur:
#             count += 1
#
#         else:
#             if count == 1:
#                 res += str(cur)
#             else:
#                 res += str(count) + "|" + str(cur)
#
#             res += ":"
#             count = 1
#             cur = el
#
#     # finalization
#     if count > 1:
#         res += str(count)
#         res += "|"
#         res += str(cur)
#     else:
#         res += str(cur)
#
#     return res


zip_list([0,1,1,1,2,3,3,4,4,4,4])
zip_list([0,1,2,3,4])
zip_list([0])
zip_list([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
zip_list([9,64,64,64,77,3,3,4,5,5,5,5,1,1,1,2,3,4,5,6,6,6])