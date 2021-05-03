# class for user-defined exception handling
class error(Exception):
    def __init__(self, a):
        self.msg = "The number "+str(a)+" is not divisible by 2!!"
  
# helper function
def util_func(a):
    try:
        if a % 2 != 0:
            raise error(a)
        return(a)
    except error as e:
        print(e.msg)
  
  
# input list
li = [2, 43, 56, -78, 12, 51, -29, 17, -24]
  
# list comprehension to choose numbers
# divisible by 2
new_li = [util_func(x) for x in li]
  
print("\nThe new list has :", new_li)