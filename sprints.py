#!/usr/bin/env python3
def MyFunc(*mylist):
    intlist = []
    floatlist = []
    sumofint = 0
    for i in mylist:
        if isinstance(i, int):
            intlist.append(i)
        elif isinstance(i, float):
            floatlist.append(i)
        else:
            return 0
    for i in intlist:
        sumofint += i
    meanOfInt = sumofint / len(intlist)
    maxOfFloat = max(floatlist)
    return meanOfInt, maxOfFloat

meanOfInt, maxOfFloat = MyFunc(1, 2, 4.3, 3, 4, 5.3, 1.4)
