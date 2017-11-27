# Bubble Sort
# We need to sort a list
# 6,24,19,1,20
# To do this we compare two elements and decide which is the larger
# Then we swap them and repeat till our list is sorted.

# define a function for our bubble sort
def bubbleSort(mylist): # we are going to pass a list to the function
    moreSorting = True # we will need to check if there is more to sort
    while moreSorting: # if True then sort
        moreSorting = False
        # we sort for the length of the list less
        # 1 as we start from 0
        for element in range(len(mylist)-1):
            # now set condition
            if mylist[element] > mylist[element + 1]:
                # the for loop is still running so there
                # is more to sort
                moreSorting = True
                # create temp variable to hold value
                temp = mylist[element]
                mylist[element] = mylist[element + 1] # swap values
                mylist[element + 1] = temp # use temp to put back value
    return mylist # give back the sorted list

# define a function to test our bubble sort
def testBubbleSort():
    mylist = [6, 24, 19, 1, 20]
    sortedlist = bubbleSort(mylist) # This calls bubbleSort()
    # sortlist will hold the content RETURNed from bubbleSort()
    print(sortedlist)

# NOW CALL OUR TEST FUNCTION TO START THE PROGRAM
testBubbleSort()