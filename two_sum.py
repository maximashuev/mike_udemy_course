def two_sum(nums:list,target:int):
    for i in range(len(nums[:-1])):
        # print(i)
        if target==(nums[i]+nums[i+1]):
            print("truse")
            print([i,i+1])
            return ([i,i+1])


two_sum([3,2,1515,5,1],6)
two_sum([3,2,3],6)