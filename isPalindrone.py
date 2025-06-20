# isPalindrone
"""
Given an integer x, return true if x is a , and false otherwise.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstrR = str(x)[::-1]
        return (str(x) == xstrR)
            

        
