list1 = [2, 6, 41, 1, 58, 33, -7, 90]
list2 = [1, 3, 2, 0, 6, 3, 7, 0]
  
  
def util_func(a, b):
    try:
        return round(a/b, 3)
    except ZeroDivisionError as e:
        print("Division by zero not permitted!!!")
  
  
list3 = [util_func(x, y) for x, y in zip(list1, list2)]
  
print(list3)