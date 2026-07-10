'''
Q1. Two Sum

Hint-
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''


class Solution:
    # Brute force solutions---------------------------
    # time complexity: O(n pow(2))

    def twosum1(self, array: list[int], target: int):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if (array[i] + array[j] == target):
                    return (i, j)
        return f"No matching element found"
    
    # Optimised Way-------------------------------
    # time complexity: O(n)
    # by using hash maps

    def twosum2(self, array: list[int], target: int):
        seen = {}
        for index, num in enumerate(array):
            diff = target - num

            if diff in seen and seen[diff] != index:
                return seen[diff], index
            
            seen[num] = index
        return f"No matching element found"


arr = [3, 2,6]
target = 9

towsum = Solution()

a = towsum.twosum1(arr, target)
b = towsum.twosum2(arr, target)
print(a)
print(b)
