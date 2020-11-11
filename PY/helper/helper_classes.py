








#1
class Person():
    pass

person = Person()

first_key = 'parametro'
first_val = 'argumento'

setattr(person, first_key, first_val)
print(getattr(person, first_key))

#2
# class Person():
#     pass

person_info = {'paramter1':'arg1', 'paramter2':'arg2'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))


