# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 03
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project attempts to meet the requirements laid out in the document
# Citations: 
# Anything else that's relevant: My test has been commented on on line 41

from functionAssign03Package.functionAssign03 import *  # importing the function from the package
count_passed = 0
count_failed = 0
if (is_divisible(15) == True):
    print("Test #1 passed")
    count_passed = count_passed + 1
else:
    print("Test #1 FAILED")
    count_failed = count_failed + 1

if (is_divisible(1) == False):
    print("Test #2 passed")
    count_passed = count_passed + 1
else:
    print("Test #2 FAILED")
    count_failed = count_failed + 1

if (is_divisible(5) == False):
    print("Test #3 passed")
    count_passed = count_passed + 1
else:
    print("Test #3 FAILED")
    count_failed = count_failed + 1

if (is_divisible(0) == True):
    print("Test #4 passed")
    count_passed = count_passed + 1
else:
    print("Test #4 FAILED")
    count_failed = count_failed + 1

if (is_divisible(22) == False):  # This is my test case
    print("Test #5 passed")
    count_passed = count_passed + 1
else:
    print("Test #5 FAILED")
    count_failed = count_failed + 1

print(str(count_passed) + " tests passed and " + str(count_failed) + " tests failed")




