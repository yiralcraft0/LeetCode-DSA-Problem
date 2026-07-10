"""
34. Find First and Last Position of Element in Sorted Array
Medium

    hint---
        Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.

    Example 1:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]

    Example 2:
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

    Example 3:
        Input: nums = [], target = 0
        Output: [-1,-1]
"""

class Solution:
    # Brute force solutions---------------------------
    # time complexity: O(n)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
            
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                second = first

                while second + 1 < len(nums) and nums[second + 1] == target:
                    second += 1

                return [first, second]
                
        return [-1, -1]
    
    # Optimised Way-------------------------------
    # time complexity: O(logn)
    # by using binary search
    def searchRange2(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        
        low = 0
        high = len(nums) 

        while low <= high:
            mid = low + (high - low) // 2
            midL = mid
            midR = mid
            if nums[mid] == target:
                while (midL - 1) >= 0 and nums[midL - 1] == target:
                    midL -= 1
                while (midR + 1) < len(nums) and nums[midR + 1] == target:
                    midR += 1

                return [midL, midR]
            elif nums[mid] > target:
                high  = mid - 1
            else:
                low = mid + 1
        return [-1, -1]

        
# nums = [4,5]
nums = []
target =4

print(f'{Solution().searchRange(nums , target)}')
print(f'{Solution().searchRange2(nums , target)}')
