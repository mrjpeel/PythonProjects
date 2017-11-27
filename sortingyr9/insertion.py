# http://courses.cs.vt.edu/csonline/Algorithms/
# Lessons/InsertionCardSort/
# insertioncardsort.html

def insertionsort(mylist):
    for element in range(1, len(mylist)):

        currentvalue = mylist[element]
        position = element

        while position > 0 and mylist[position -1]> currentvalue:
            mylist[position] = mylist[position -1]
            position = position - 1

        mylist[position] = currentvalue
    return mylist


def testinsertionsort():
    mylist = [34,2,36,78,12]
    sortlist = insertionsort(mylist)
    print(sortlist)

testinsertionsort()