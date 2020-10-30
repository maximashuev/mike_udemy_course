def check(input:tuple):
    # print(type(input))
    for i in input[0]:
        print(i)
        if input[1]== i:
            print("True")


check([[1,2,3,4],3])