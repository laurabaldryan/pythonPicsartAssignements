import inspect 

def my_reduce(func,iterable):
    signature=inspect.signature(func)
    numbers=signature.parameters
    if len(numbers)==2:# checking binary function condition
        sum=iterable[0]
        for i in range(1,len(iterable)):
            sum=func(sum,iterable[i])
            yield sum

ls=[4,4,4,4,4]

print(list(my_reduce(lambda x,y :x+y, ls)))

