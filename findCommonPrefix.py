# findCommonPrefix
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # starting word and length
        prefix = strs[0]
        prefix_length = len(prefix)

        # loop through all other words
        for c in strs[1:]:
            # while prefix not equal to starting prefix or prefix after update
            while not c.startswith(prefix):
                # shorten prefix length
                prefix_length -= 1
                if prefix_length == 0:
                    return ""
                # update prefix
                prefix = prefix[0:prefix_length]
                
        return prefix
