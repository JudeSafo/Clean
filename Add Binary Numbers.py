"""
Author: Jude Safo
Title: Add two binary string numbers (without using built-ins)

**note: the author is aware of the optimal alternatives, this solution however
is for the sole purpose of carrying out an earlier attempt at the problem with the
same method.
"""

from typing import List
from functools import reduce

class InvalidString(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

class BinaryAddition:
    def __init__(self, n1: str = None, n2: str = None):
        self.n1 = n1
        self.n2 = n2
    """
    This module simply adds two binary number
    non-negative, integer numbers together. 

    Time: O(max(len(n1), len( n2))
    Space: O(max(len(n1), len( n2))
    >> n1, n2 = "1101", "10101100"
    >> B = BinaryAddition(n1, n2)
    >> B.addBinary()
    '01010111'
    """
    def addBinary(self, n1: str = "1101", n2: str = "10101100") -> str:
        if self.n1 and self.n2:
            n1, n2 = self.n1, self.n2

        if not any([n1,n1]):
            raise InvalidString("Empty String Entered")

        output, stack = [], self._process(n1, n2)
        for x, y in stack[::-1]:
            output.append(self._add(x,y))
        ans = "".join(str(_) for _ in output[::-1])
	#TODO: correct self._carry method to handle 3 input gates
        """while stack:
            x, y = stack.pop()
            output.append(self._carry(stack, x, y, None)) """

        #Unit test
        assert bin(int(n1,2)) + bin(int(n2,2)) == bin(int(ans)),"Incorrect Solution"
        return ans

    # Process the raw binary strings
    def _process(self, n1: str, n2: str) -> List[tuple]:
        if self.n1 and self.n2:
            n1, n2 = self.n1, self.n2

        # combine raw string inputs return int array in correct order
        nums_array = sorted([list(n1), list(n2)], key = len, reverse = True)       #adds an additional O(nlogn) to run time; bottleneck
        prepend = ['0']*(len(nums_array[0]) - len(nums_array[1]))
        nums_array[1] = prepend + nums_array[1]
        nums_array = [(int(x), int(y)) for x, y in list(zip(*nums_array))]
        return nums_array

    #carry: without using %2 operation
    def _carry(self, stack: List[tuple], x: int, y: int, z: int = None) -> str:
        carry = self._add(x, y, z)
        if len(carry) > 1:
            x, y = stack.pop()
            z = int(carry[1])
            return self._carry(stack, x, y, z)
        return carry

    #add two binary numbers return string
    def _add(self, x: int, y: int, z: int = None) -> str:
        f = lambda x,y: str(int('0b0',2))*(~x&y) + str(int('0b1',2))*(x^y) + str(int('0b1010',2))*(x&y)
	# Unit test
	assert list(map(f,(0,0,1,1),(0,1,0,1))) == ['0', '1', '1', '10'], "Logic test failed"
	if not z:
            return f(x,y)

	#TODO: fix logic to handle 3 input gates
        return reduce(f(x,y), [x, y, z])

B = BinaryAddition("1101","10101100")
print(B.addBinary())
