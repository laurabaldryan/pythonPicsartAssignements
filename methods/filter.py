def my_filter(func,iterable):
    if func==None:
        for i in iterable:
            yield i
    for i in iterable:
        yield func(i)

def func(n):
    return n*2

ls=[2,4,6,8]

print(ls)
print(list(my_filter(func,ls)))

