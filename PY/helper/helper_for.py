









#1
names = ['gui', 'simone', 'julia']

for index, name in enumerate(names, start = 1):
    print(index, name) 


#2 (Not so good)
names = ['Peter Parker', 'Clark Kent', "Bruce Wayne"]
heroes = ['Spiderman', 'Sperman', 'Batman']

for i, e in enumerate(names):
    hero = heroes[i]
    print(f'{e} is actually {hero}')


#3  ( Better )
names = ['Peter Parker', 'Clark Kent', "Bruce Wayne"]
heroes = ['Spiderman', 'Sperman', 'Batman']
universe = ['Marvel', 'DC', 'DC']

for i, e, u in zip(names, heroes, universe):
    print(f'{i} is actually {e} from {u}')

