'''
Q11. Container With Most Water
Medium

Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

class Solution:
    # Brute force solutions---------------------------
    # time complexity: O(n pow(2))

    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        length = 0
        breadth = 0

        for i,j in enumerate(height):
            for k,l in enumerate(height):
                if j > l:
                    length = l
                else:
                    length = j

                breadth = k - i
                area = length * breadth
                if (area > maxarea):
                    maxarea = area
        return maxarea
    
    # Optimised Way solutions---------------------------
    # By two pointer
    # time complexity: O(n)

    def maxArea2(self, height: list[int]):
        maxarea = 0
        length = 0
        breadth = 0
        i = 0
        j = len(height) - 1

        for _ in range(len(height)):
            if height[i] < height[j]:
                length = height[i]
                i += 1
            else:
                length = height[j]
                j -= 1
            
            breadth = (j + 1) - i
            area = length * breadth

            if (area > maxarea):
                maxarea = area
        return maxarea
            
        
MaxArea = Solution()

heights = [9,1,8,6,2,5,4,8,3,7,9]

print(MaxArea.maxArea(heights))
print(MaxArea.maxArea2(heights))