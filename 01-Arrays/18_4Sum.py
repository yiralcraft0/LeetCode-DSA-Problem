"""
18. 4Sum
Medium

Given an array nums of n integers, return an array of all the 
unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

# Optimised Way solutions------------------------------------------------
# time complexity: O(n pow(3))
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(n - 1, i, -1):
                l, r = i + 1, j - 1
                while l < r:
                    if i != j:
                        total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target and [nums[i], nums[j], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])

                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return ans
    
    # More faster in millisec

    def fourSum2(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif total < target:
                        l += 1

                    else:
                        r -= 1
        return ans


solve = Solution()

nums = [-3, -1, 0, 2, 4, 5]
target = 0

print(f'{solve.fourSum(nums, target)}')
print(f'{solve.fourSum2(nums, target)}')
