import time
def timer(f):
    def inner(*args, **kargs):
        t = time.time()
        ret = f(*args, **kargs)
        print('timer = %s' %(time.time()-t) )
        return ret
    return inner

@timer
def my_fnc():
    pass

if __name__ == '__main__':
    my_fnc()


