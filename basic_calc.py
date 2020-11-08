#Title: Basic Calc
#Author: Jude Safo

from typing import List
from functools import reduce
import re

class basicCalc:
    def __init__(self, s: str):
        self.s = s

    def string_to_int(self, arg: str = ""):
        #map strings to int
        if not arg:
            arg = self.s
        return list(map(int, arg))

    def helper(self, operator: str = "", summand: int = 0):
            #perform the appropriate operation
            if operator == '+':
                return reduce(lambda x, y: x + y, summand)

            elif operator == '*':
                return reduce(lambda x, y: x*y, summand) 

    def postorder(self, s1: str = "") -> str:
        # postorder traversal of binary tree
        try:
            query = re.search(r"\(([+*])(.*)\)$", s1)
        except:
            return s1

        # basecase
        search = query.groups(1)
        if not search[1]:
            return self.helper(search[0], self.string_to_int(search[1]))
        return self.postorder(search[0]) + self.postorder(search[1]) + search[1]
    

#s = "(* 12345)"
#s = "(* (+ (* (+ 543) 2) 12) 4)"
s = "(* 1 (+ 2 (* 3 (+ 543))))"
BC = basicCalc(s)
summand = BC.string_to_int(list(map(str,range(4,10))))
print(BC.helper('*', summand))
print(BC.helper('+', summand))
print(BC.postorder(s))
