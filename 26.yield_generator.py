def my_generator(value: int, power: int, amount: int):
    while amount>0:
        yield value**power
        amount-=1
        value+=1



gen=my_generator(12,2,5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))