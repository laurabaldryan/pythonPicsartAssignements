def my_zip(*iterables):
    if iterables==None:
        print("Error")
        return
    minLength=len(iterables[0])
    for i in range(1,len(iterables)):
        if minLength>len(iterables[i]):
            minLength=len(iterables[i])
    for i in range(minLength):
        yield tuple((j[i] for j in iterables))

ls1=[1,2,3,4,5]
ls2=['a','b','c']
ls3=[2,3,4,5]

print(list(my_zip(ls1,ls2,ls3)))
