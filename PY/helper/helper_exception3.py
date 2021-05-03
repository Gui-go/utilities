li = ['10', '11', 7, 'abc', 'cats', 3, '5']
  
# helper function
def util_func(a):
    try:
        return int(a)*int(a)
    except ValueError:
        pass
  
  
# list comprehension
new_li = [util_func(x) for x in li]
  
print(new_li)