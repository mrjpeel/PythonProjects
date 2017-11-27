def bubblesort(mylist):
    moresorting = True
    while moresorting:
        moresorting =False
        for element in range(len(mylist)-1):
            if mylist[element] > mylist[element + 1]:
                moresorting = True
                temp = mylist[element]
                mylist[element] = mylist[element + 1]
                mylist[element + 1] = temp
    return mylist

def testbubblesort():
    mylist = [6, 24, 19, 1, 20]
    sortedlist = bubblesort(mylist)
    print(sortedlist)

testbubblesort()