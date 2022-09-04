#!/usr/bin/env python3
import sprints

print("________First test case_________")
TestList=[1,2,4.3,3,4,5.3,1.4]
meanOfInt, maxOfFloat = sprints.MyFunc(TestList)
print("mean of integers:",meanOfInt) # mean should be 1+2+3+4/4 -> 2.5
print("maximum of floats:",maxOfFloat)# max float shoud be 5.3

print("________Second test case_________")
TestList=[10,10.5,20,25,60.7,100.0]
meanOfInt, maxOfFloat = sprints.MyFunc(TestList)
print("mean of integers:",meanOfInt) # mean should be 10+20+25/3 -> 18.333333
print("maximum of floats:",maxOfFloat)# max float shoud be 100.0
