from ru_loc import *
import math
import turtle

def get_num_hexagons():
    '''Input validation for number hexagons'''
    while True:
        n = input(NUMBER_INPUT)
        if not n.isdigit():
            print(REWRITE_NUMBER)
        elif int(n) < 4 or int(n) > 20:
            print(REWRITE_NUMBER)
        else:
            break
    return int(n)
