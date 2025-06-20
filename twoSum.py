# twoSum
"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            # x = target - num
            x = target - num
            if x in num_dict:
                return[num_dict[x], i]
            num_dict[num] = i
