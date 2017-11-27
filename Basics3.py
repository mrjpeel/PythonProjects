
''' A WHILE Loop will always test against a TRUE
condition '''

count = 0

while count < 5:
    print(count)
    count = count +1 # count += 1

# From the above I expect to see 0,1,2,3,4

''' A FOR Loop will execute the code a set number
of times '''

''' for ITEM in SOMETHING:
        do something...'''

for letter in 'Jason':
    print(letter)
# the above will print each letter of the string

for item in range(3,6):
    print(item)
# the above will print 3,4,5

for item in range(5):
    print(item)
# the above will print 0,1,2,3,4

animals =  ['mouse', 'cat','dog','sheep']
for item in range(len(animals)):
    print(item, animals[item])

''' Above we created a list.  We then found the LENgth of
the list and printed out the position in the list and 
the individual animals from the list e.g. 0 mouse 1 cat ...'''

''' A DO WHILE will work at least once.'''
# PYTHON DOES NOT HAVE A DO WHILE
# SO HERE IS A JAVASCRIPT VERSION
'''
    var i = 0;
    do {
        i += 1;
        console.log(i);
    } while (i <5);
'''

#  MORE HELP https://docs.python.org/3/tutorial/controlflow.html