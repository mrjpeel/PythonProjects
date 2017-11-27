# start a new python file called insertion
# https://goo.gl/aniJOQ
# The link above is the animation of how insertion sort works

# define a function for insertion sort
def insertionsort(mylist): # Give the function a list to sort mylist
    for element in range(1, len(mylist)):
        # Get the first element in to a variable
        currentvalue = mylist[element]
        # set the marker to divide the sorted with unsorted
        marker = element
        # now start swapping the elements as needed
        while marker > 0 and mylist[marker - 1] > currentvalue:
        # We need to check the final position of the value
        # with every element in the sorted section
        # so we use another loop to do this a WHILE loop
            mylist[marker] = mylist[marker - 1]
            marker = marker - 1
        #now set the new current value
        mylist[marker] = currentvalue
    # Finally give back the sorted list, the sorted list is RETURNed to sortlist variable
    return mylist


def testinsertionsort():
    print("I need a list to sort.")
    morenums = True
    mylist = []
    while morenums:
        getnum = input('''Please enter a number followed by enter.  \n''')
        if getnum.isalpha() == True:
            print('Thank you, ')
            break
        else:
            mylist.append(int(getnum))
    print('Your unsorted list is', mylist)
    sortlist = insertionsort(mylist) # Create a variable to hold the sorted list
    print('Your sorted list is', sortlist) # print out the answer

# This will call the test function and is the start of my program
testinsertionsort()