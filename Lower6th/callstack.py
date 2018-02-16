def printList(num):
    num = num - 1
    if num > 1: printList(num)
    print("at Line B, num =", num)

x = 4
printList(4)
print("At Line A, x = ", x)