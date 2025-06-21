# validParentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in range(len(s)):
            x = s[i]
            if x in "[{(":
                temp.append(x)
            else:
                if not temp:
                    return False
                y = temp.pop()
                if y == "[" and s[i] != "]":
                    return False
                elif y == "(" and s[i] != ")":
                    return False
                elif y == "{" and s[i] != "}":
                    return False
        return len(temp) == 0
