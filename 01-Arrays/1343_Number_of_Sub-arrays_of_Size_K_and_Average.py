"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Medium
    Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

    Example 1:
        Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        Output: 3
        Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

    Example 2:
        Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
        Output: 6
        Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
"""

class Solution:
    # Optimised Way-------------------------------
    # time complexity: O(n)
    # by using Sliding Window

    def numfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        arrCount = 0

        left = 0
        right = k - 1

        while True:
            avg = total / k

            # print(f'TOTAL : {total}')
            # print(f'AVG : {avg}')

            if avg >= threshold:
                arrCount += 1
            
            if (right + 1) < len(arr):
                total -= arr[left]
                left += 1
                right += 1
                total += arr[right]
            else:
                break

            # print(f'LEFT : -{arr[left]}')
            # print(f'RIGHT : +{arr[right]}')

        return arrCount
    
    def numfSubarrays2(self, arr: list[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        arrCount = 0

        if total/k >= threshold:
                arrCount += 1

        left = 0
        for right in range(k , len(arr)):
            total -= arr[left]
            total += arr[right]
            left += 1

            if total/k >= threshold:
                arrCount += 1

        return arrCount

arr = [2,2,2,2,5,5,5,8]
k = 3       
threshold = 4

print(f'{Solution().numfSubarrays(arr , k , threshold)}')
print(f'{Solution().numfSubarrays2(arr , k , threshold)}')

