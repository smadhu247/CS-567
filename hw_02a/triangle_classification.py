# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(arg_a,arg_b,arg_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    invalid = False
    bad_type = False

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(arg_a,int) and isinstance(arg_b,int) and isinstance(arg_c,int)):
        invalid = True
        bad_type = True

    if bad_type is False:
        # require that the input values be >= 0 and <= 200
        if arg_a > 200 or arg_b > 200 or arg_c > 200:
            invalid = True

        if arg_a <= 0 or arg_b <= 0 or arg_c<= 0:
            invalid = True

    if invalid is True:
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (arg_a > (arg_b + arg_c)) or (arg_b > (arg_a + arg_c)) or (arg_c > (arg_a + arg_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if arg_a == arg_b and arg_b == arg_c:
        return 'Equilateral'
    if ((arg_a ** 2) + (arg_b ** 2)) == (arg_c ** 2) or \
        ((arg_b ** 2) + (arg_c ** 2)) == (arg_a ** 2) or \
        ((arg_a ** 2) + (arg_c ** 2)) == (arg_b ** 2):
        return 'Right'
    if arg_b not in (arg_a, arg_c) and arg_a not in (arg_b, arg_c)and arg_c not in (arg_a, arg_b):
        return 'Scalene'
    return 'Isoceles'
