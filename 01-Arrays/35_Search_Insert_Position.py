'''
35. Search Insert Position
Easy
    Hint----
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

    Example 1:
        Input: nums = [1,3,5,6], target = 5
        Output: 2

    Example 2:
        Input: nums = [1,3,5,6], target = 2
        Output: 1
        Example 3:

    Example 3:
        Input: nums = [1,3,5,6], target = 7
        Output: 4
'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high  = mid - 1
            else:
                low = mid + 1

        return low
        

nums = [2,4,6,8]

target = 0

print(f'{Solution().searchInsert(nums , target)}')
