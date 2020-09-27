﻿“””
Author: Jude Safo
Title: Add two binary string numbers (without using built-ins)

**note: the author is aware of the optimal alternatives, this solution however
is for the sole purpose of carry out a earlier attempt at the problem with the
same method.
“””

from typing import List

class InvalidString(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

class BinaryAddition:
    def __init__(self, n1: str = None, n2: str = None):
        self.n1 = n1
        self.n2 = n2

    def addBinary(self, n1: str = "1101", n2: str = "10101100") -> str:
        if self.n1 and self.n2:
            n1, n2 = self.n1, self.n2

        if not any([n1,n1]):
            raise TestFailed("Empty String Entered")

        output, stack = [], self._process(n1, n2)
        for x, y in stack:
            output.append(self._add(x,y))
        ans = "".join(str(_) for _ in output[::-1])
        """while stack:
            x, y = stack.pop()
            output.append(self._carry(stack, x, y, None)) """

        #Unit test
        assert bin(int(n1,2)) + bin(int(n2,2)) == bin(int(ans)),"Incorrect Solution"
        return ans

    # Process the raw binary strings
    def _process(self, n1: str, n2: str) -> List[tuple]:
        if self.n1 and self.n2:
            n1,n2 = self.n1, self.n2

        # combine raw string inputs return int array in correct order
        nums_array = sorted([list(n1), list(n2)], key = len, reverse = True)
        prepend = ['0']*(len(nums_array[0]) - len(nums_array[1]))
        nums_array[1] = prepend + nums_array[1]
        nums_array = [(int(x), int(y)) for x,y in list(zip(*nums_array))]
        return nums_array

    #carry: without using %2 operation
    def _carry(self, stack: List[tuple], x: int, y: int, z: int = None) -> str:
        carry = self._add(x, y, z)
        if len(carry) > 1:
            x, y = stack.pop()
            z = int(carry[1])
            return self._carry(stack, x, y, z)
        return temp

    def _add(self, x: int, y: int, z:int = None) -> str:
        if not z:
            return "0"*(~x&y) + "1"*(x^y) + "01"*(x&y)

        #TODO: refine logic
        nums = [str(_) for _ in [x,y,z]]
        reduce((lambda x, y: "0"*(~x&y) + "1"*(x^y) + "01"*(x&y)), nums)

B = BinaryAddition("1101","10101100")
print(B.addBinary())