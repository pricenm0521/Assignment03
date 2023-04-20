# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 03
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project attempts to meet the requirements laid out in the document
# Citations: https://www.w3resource.com/python-exercises/python-basic-exercise-147.php
# Anything else that's relevant: Remembering when to use % sign for division is hard

def is_divisible(number):
    '''
    Write a function that accepts an integer and returns a boolean
    Return true if divisible by 3 and 5, otherwise return false
    '''
    number = int(number)
    return True if number % 3 == 0 and number % 5 == 0 else False

