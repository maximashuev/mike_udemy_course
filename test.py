def er(array):
    temp=len(array)-1
    print(temp)
    after=[]
    while temp>=0:
        after.append(array[temp])
        temp-=1
    print(after)
er([1,2,3,4,5])