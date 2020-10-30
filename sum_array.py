def sum_array(input:list):
    sum1=input[1]+input[0]+input[2]+input[3]+input[4]
    print(sum1)

    sum2=sum(input)
    print(sum2)

    sum3=0
    for i in range(len(input)):
        sum3=sum3+input[i]
    print(sum3)





sum_array([1,2,3,4,5])