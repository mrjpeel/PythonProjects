def mergeSort(alist):
    print("Splitting ",alist)
    # check is the list bigger than 1
    if len(alist)>1:
        mid = len(alist)//2 # WHY TWO // ?
        lefthalf = alist[:mid] # [:mid] start to mid
        righthalf = alist[mid:] # [mid:] mid to start
        mergeSort(lefthalf) # recursive use of mergesort function
        mergeSort(righthalf) # left then right list
        i=j=k=0 # create 3 variables equal to zero
        # 0 < length of leftlist AND 0 < length of rightlist
        while i < len(lefthalf) and j < len(righthalf):
        # check each element of left vs right
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i] # add left int back to main list
                i=i+1 # go to next element
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)





alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
