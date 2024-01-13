print('hello world')

var = 'Tulaib Mirza'
type(var)

int_var = 12
type(int_var)

#Float
float_var = 12.0
type(float_var)

#Boolean
bool_var = True
print(bool_var)
type(bool_var)

#String Manipulation



#Integer
print(1+2)

#Floats
print(0.1 + 0.1)

#Data Types

#Constants
MAX_CONNECTION = 5000

#List
#Is dynamic in nature
#Can store multiple values
list_ = [1,3,3,4]

#Dictionary
dict_ = {'key':'value'}

#Tuple
tuple_ = (1,3,4,4,'s',1.0)

#Sets
#Stores unique values
sets_ = {2,3,4,1,1}
print(sets_)


#looping
#first value is start, second is range, third is steps
for i in range(1,10,2):
    print(i)

names = ['Mirza', 'Tulaib', 'Yasir']
for name in names:
    print(name)

for char in 'tulaib':
    print(char)

for i in range(0,len(names)):
    print(i, names[i])

for i, name in enumerate(names):
    print(f'hello {name}, at index {i}')


cars = ['civic', 'corolla', 'corvette', 'gtr']
for i, car in enumerate(cars):
    print(f'{car}, {i}')


#Temp
index = [2,0,3,1]
temp = []
for i in index:
    temp.append(cars[i])
print(temp)

', '.join(cars)


'awais'[::-1]
print(cars)
cars[1:4:2]

#if statement

for cars in cars:
    if car == 'gtr':
        print(car.upper())
    else:
        print(car.title())


#Checking Wheteher a Value is in a list
        
requested_toppings = ['mushrooms', 'onions', 'pineapples']

'mushrooms' in requested_toppings



#items will print both
favorite_languages = {
    'mirza': 'python',
    'tulaib': 'java',
    'yasir': 'javascript',
    'irfan': 'php'
}

for obj in favorite_languages.items():
    print(obj)

for key, value in favorite_languages.items():
    print(key, value)

for key, value in favorite_languages.items():
    print(f"{key}'s favorite language is {value}")


favorite_languages = {
    'mirza': ['python', 'SQL'],
    'tulaib': ['java', 'kotlin'],
    'yasir': ['javascript'],
    'irfan': ['php', 'mysql']
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is:")
    if isinstance(languages, list):
        for language in languages:
            print(language)
    else:
        print(languages)
    
    #arbitary arguments
    def make_pizza(*toppings):
        for topping in toppings:
            print(topping)

