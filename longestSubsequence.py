"""
test for empty strings? 
test for single char?
test for identical chars ==> should return len(s)
data type checks? 
max length of string? 
are these char only? (or alphanumeric)

high level:
s: "babad"
    ^
l: 0
r: 5
max_pal: 0

options:
1. dp   0(n^2)
2. binary search (e.g. 2 pointers) - build substring from the middle outward    0(n)
3. math - valid palindrome (e.g at most 1 odd freq, char) - can add math check before running 0(n)
4. brute force - perform all permuations and test (0(n!)

helpers:
1. bool isPal -  (test sub == sub[::-1])

"""
class helpers:
    def isPal(self, i: int, j: int) -> bool:
        #flip and compare they're identical
        return self.s[i:j] == self.s[i:j][::-1]
    
    def isOddCheck(self, i: int, j: int) -> bool:
        #ensure odd char freq doesn't exceed 1
        counts = Counter(s)
        return sum(map(lambda x: not ~x & 1, counts.values())) < 2
    
    def dpSoln(self):
        # iterate through string (while creating substrings centered from that position, keeping track of the max len
        n, dp = len(self.s), {}
        
        for i in range(len(self.s) - 1, -1, -1):
            for j in range(i):
                if self.isPal(i,j):
                    dp[i] = max(dp.setdefault(i, ""), 
                                dp.get(i - j, "") + self.s[i:j], key = len)
        #print(dp)
        return dp[n - 1]
    
    def mathSoln(self) -> str:
        # itertate through all substring permutations while checking is odd
        all(self.isOdd(i, j) for i in range(len(s))
                                for j in range(i))
    
    def bruteForce(self) -> str:
        all(self.isPal(i,j) for i in range(len(s))
                                for j in range(i))
        
class Solution(helpers):
    def longestPalindrome(self, s: str) -> str:
        assert isinstance(s, str), "sanity check"
        self.s = s
        
        # save run time, test limits
        if len(set(self.s)) == len(self.s) or len(self.s) == 1:
            return self.s
        
        return self.dpSoln()  
    
#Run Test Cases
S = Solution ()
"""
assert S.longestPalindrome("babad") == "bab", "base-case"
assert S.longestPalindrome("a") == "a", "single char"
assert S.longestPalindrome("ac") == "a", "odd count case"
"""
