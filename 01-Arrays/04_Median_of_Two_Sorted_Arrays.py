'''
Q4. Median of Two Sorted Arrays----------

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

'''


class Solution:
    # Brute force solutions---------------------------
    # time complexity: O((m+n)log(m+n))

    def findMedianSortedArrays(self, num1: list[int], num2: list[int]):
        nums = num1[:]  # O(n)

        for i, j in enumerate(num2):  # O(m)
            nums.append(j)

        nums.sort()                   # Tim Sort O(nlogn)

        numsLen = len(nums)
        if numsLen % 2 == 0:
            i1 = int(numsLen / 2)
            i2 = int(i1 - 1)
            median = (nums[i1] + nums[i2]) / 2
            return median
        else:
            i1 = int((numsLen - 1)/2)
            median = nums[i1]
            return median

    # Optimised Way-------------------------------
    # Two Pointer
    # time complexity:

    def findMedianSortedArrays2(self, num1: list[int], num2: list[int]) -> float:
        len1, len2 = len(num1), len(num2)
        numsLen = len1 + len2
        
        i, j = 0, 0
        current = 0
        previous = 0
        
        for _ in range((numsLen // 2) + 1):
            previous = current
    
            if i < len1 and (j >= len2 or num1[i] <= num2[j]):
                current = num1[i]
                i += 1
            else:
                current = num2[j]
                j += 1
        if numsLen % 2 != 0:
            return float(current)
        return (previous + current) / 2.0

# Have to do more practise for more better solution

num1 = [1, 5, 6,10]
num2 = [3, 4,7,9]
[1,3,4,5,6,7,9,10]
solev = Solution()

print(f"{solev.findMedianSortedArrays(num1, num2)}")
print(f"{solev.findMedianSortedArrays2(num1, num2)}")
