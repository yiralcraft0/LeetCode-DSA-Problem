'''
189. Rotate Array
Medium
    
    Hint-------------
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Example 1:-------
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:-----------
        Input: nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation: 
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]
'''

class Solution:
    # Time Complexity: O(n) (each element reversed at most twice)
    # Space Complexity: O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return
        
        arrLen = len(nums)
        k %= arrLen

        low1 = arrLen - k
        high1 = arrLen - 1
        while low1 <= high1:

            nums[low1] , nums[high1] = nums[high1], nums[low1]
            low1 += 1
            high1 -= 1

        low2 = 0
        high2 = (arrLen - k) - 1
        while low2 <= high2:

            nums[low2] , nums[high2] = nums[high2], nums[low2]
            low2 += 1
            high2 -= 1
        
        low3 = 0
        high3 = arrLen - 1
        while low3 <= high3:

            nums[low3] , nums[high3] = nums[high3], nums[low3]
            low3 += 1
            high3 -= 1

        return nums
    
    # Simplify Version (Same logic and Time complexity)

    def rotate2(self, nums: list[int], k: int) -> None:
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        arrLen = len(nums)
        k %= arrLen

        reverse(0, arrLen - 1)
        reverse(0, k - 1)
        reverse(k, arrLen - 1)


nums = [1,2]
k = 50
print(f'{Solution().rotate(nums, k)}')
print(f'{Solution().rotate2(nums, k)}')
