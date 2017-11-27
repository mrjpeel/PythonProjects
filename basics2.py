''' CONDITIONS '''

''' Conditions allow us to check if something is right or not '''

# create a variable.

x = 2

print(x == 2)
print(x == 3)
print(x > 3)

print( x != 2) # What will the outcome be?
print(x <= 2)
print(1 <= x)

name = 'John'
age = 67

''' SELECTION or making decisions with CONDITIONS'''

if name == 'John'  and age == 67:
    print("Hello " + name + " I didn't know you were " + str(age) )
else:
    print('Who are you?')

if name =='John' or name == 'Rick':
    print('Hey guy')
else:
    print('What time is it?')

# What if we ask for input
# But we have more than one option
# Like in the case of if we need a yes or no?


answer = input('Do you like anime? \n')

if answer in ['yes','Yes','YES','Y','y']:
    print('Great, me too!')

elif answer in ['no','No','NO','N','n']:
    print('thats a shame, perhaps you just havent seen the right one for you?')

else:
    print('Sorry I needed a yes or no and you answered', answer)