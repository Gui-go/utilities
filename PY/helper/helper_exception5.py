# class for user-defined exception handling
class error(Exception):
    def __init__(self, a):
        self.msg = "The number "+str(a)+" is not in range!!!"
  
# helper function
def util_func(a):
    try:
        if a < 10 or a > 20:
            raise error(a)
        return(a)
    except error as e:
        print(e.msg)
        return 0
  
  
# input list
li = [11, 16, 43, 89, 10, 14, 1, 43, 12, 21]
  
# list comprehension to choose numbers
# in range 10 to 20
new_li = [util_func(x) for x in li]
  
print("\nThe new list has :", new_li)