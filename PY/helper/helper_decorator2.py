def myDecorator(func):
    def new_func(n):
        return '$' + func(n)        
    return new_func

@myDecorator
def myFunction(a):
    return(a)

# call the decorated function
print(myFunction('100'))


