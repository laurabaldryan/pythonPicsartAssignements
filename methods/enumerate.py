def enumerate1(iterable,start=0):
    for i in range(len(iterable)):
        yield start,iterable[i]
        start+=1
        

ls=['a','b','c']

print(list(enumerate1(ls,4)))
