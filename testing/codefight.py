def add(param1, param2):
    if(-100 >= param1 or param1 >= 1000):
        print('out of range', param1)
    elif(-100 >= param2 or param2 >= 1000):
        print('out of range', param2)
    else:
        return param1 + param2

add = add(-11000,-111)
print(add)