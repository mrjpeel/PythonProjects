# Make sure you comment your code
# First create a function for the algorithm

def bubblesort(listToSort):# we need to pass a list to sort
    moreSorting = True # Boolean to track sorting
    while moreSorting: # While loop to ensure everything swaps
        moreSorting = False # Stop sorting if its all done
        for element in range(len(listToSort) -1): # sort list -1
            # next check size of numbers
            if listToSort[element] > listToSort[element +1]:
        # if first is bigger than second we need to swap them
                moreSorting = True
                temp = listToSort[element] # WHY?
        # make current list number the next list number, swap them
                listToSort[element] = listToSort[element + 1]
                listToSort[element +1] = temp
    # the return will give back the result or sorted list
    return listToSort

#create test function
def testbubblesort():
    mylist = [ 4, 23, 5, 7, 355, 1, 45]
    sortedlist = bubblesort(mylist) # Use the bubblesort function
    print(sortedlist) # print our list after it is sorted


testbubblesort() # Start of program, call the test function