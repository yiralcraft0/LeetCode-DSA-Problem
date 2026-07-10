'''
Q16. 3Sum Closest
Medium

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    # Optimised Way solutions---------------------------
    # time complexity: O(n pow(2))
    
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sortNum = nums.sort()
        minDiff = float('inf')
        closeSum = 0
        
        for i in range(len(nums) - 2):

            l, r = i + 1, len(nums) - 1

            while l < r :

                total = nums[i] + nums[l] + nums[r]
                difference = abs(target - total)

                if  difference < minDiff:
                    minDiff = difference
                    closeSum = total

                if target == total:
                    return target
                
                if total > target:
                    r -= 1
                else:
                    l += 1
                
        return closeSum

solve = Solution()

nums = [-4,2,2,3,3,3]
target = 0

print(f'{solve.threeSumClosest(nums , target)}')
