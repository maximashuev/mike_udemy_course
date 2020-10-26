def sum_everything(a, b):
    if isinstance(a,int):#int,list
        print("int,list:")
        print(a+len(b))
        return(a+len(b))
    elif isinstance(a,list):
        if isinstance(b,list):#list,list
            print("list,list:")

            print(a + b)
            return a + b
        elif isinstance(b,str):#list,str
            a.append(b)
            print("list,str:")
            print(a)
            return (a)

    else:                      #str,int
        print("str,int:")
        print(a+str(b))

        return (a+str(b))




sum_everything(['q','2'],['w','5'])#list,list
sum_everything(1,["2","g","hj","2"])#int,list
sum_everything(["2","g","hj","2"],"dgnjgfjgf")#list,str
sum_everything("dgnjgfjgf",4568)#str,int
